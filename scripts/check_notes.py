#!/usr/bin/env python3
"""Validate this Markdown knowledge base and optionally regenerate its indexes.

Uses only the Python standard library. Front matter follows the template's
single-line fields, with JSON quoted strings and a JSON array for tags.
"""

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "id", "title", "type", "status", "created", "updated", "source_date",
    "verification", "tags", "summary",
}
TYPES = {"survey", "learning", "comparison", "practice", "retrospective"}
STATUSES = {"draft", "snapshot", "reviewed"}
VERIFICATIONS = {"source-review", "calculation", "simulation", "hardware", "mixed"}
MAX_FILE = 5 * 1024 * 1024
MAX_NOTE = 25 * 1024 * 1024
BANNED_EXT = set(
    ".urdf .xacro .mjcf .usd .usda .usdc .usdz .stl .obj .glb .gltf .step "
    ".stp .sldasm .sldprt .slddrw .x_t .x_b .pt .pth .ckpt .onnx .safetensors "
    ".bin .npz .npy .h5 .hdf5 .parquet .mcap .bag .db3 .zip .7z .tar .gz .xz "
    ".so .whl .log".split()
)
BANNED_DIRS = {"third_party", "official_sources", "node_modules", "models", "weights", "checkpoints", "datasets"}
SOURCE_EXT = {".py", ".cpp", ".c", ".h", ".hpp", ".rs", ".go", ".sh", ".ipynb"}
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)')
LOCAL_PATH = re.compile(r"(?:/home/|/Users/|file://|(?<![A-Za-z0-9])[A-Za-z]:[\\/])")


def read_metadata(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("缺少 front matter")
    end = lines.index("---", 1)
    result = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep or not re.fullmatch(r"[a-z_]+", key):
            raise ValueError(f"不支持的元数据格式：{line}")
        if key in result:
            raise ValueError(f"重复元数据字段：{key}")
        value = value.strip()
        result[key] = json.loads(value) if value.startswith(('"', '[')) else value
    return result


def without_fences(text):
    output = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)


def anchors(path):
    text = without_fences(path.read_text(encoding="utf-8"))
    found = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    counts = Counter()
    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        label = re.sub(r"<[^>]+>", "", heading.group(1))
        label = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", label)
        slug = re.sub(r"[^\w\- ]", "", label.lower()).replace(" ", "-")
        index = counts[slug]
        counts[slug] += 1
        found.add(slug if index == 0 else f"{slug}-{index}")
    return found


def generated_indexes(categories, notes):
    by_category = {c["slug"]: [] for c in categories}
    for path, meta in notes:
        by_category[path.parent.parent.name].append((path, meta))
    root_lines = ["# 全部笔记", "", "<!-- 自动生成；请修改主题元数据后运行 scripts/check_notes.py --write-index。 -->", "",
                  "| 分类 | 主题 | 阶段摘要 | 原研究日期 | 更新日期 |", "|---|---|---|---|---|"]
    nav = ["# 分类入口", "", "<!-- 自动生成；分类定义在 catalog.json。 -->", "",
           "按产品或算法建主题包；交叉主题使用标签和链接。", "",
           "| 分类 | 范围 | 已收录主题 |", "|---|---|---:|"]
    outputs = {}
    for category in categories:
        slug = category["slug"]
        entries = sorted(by_category[slug], key=lambda pair: pair[1]["id"])
        nav.append(f'| [{slug} · {category["title"]}]({slug}/README.md) | {category["scope"]} | {len(entries)} |')
        page = [f'# {slug} · {category["title"]}', "", "<!-- 自动生成；请勿手工编辑。 -->", "",
                category["scope"] + "。", "", "对象示例：" + category["examples"] + "。示例名称不代表已有笔记。", ""]
        if not entries:
            page += ["尚无迁入笔记。新增内容请先阅读 [Agent规范](../../AGENTS.md) 和 [贡献流程](../../CONTRIBUTING.md)。", ""]
        for path, meta in entries:
            relative = path.relative_to(ROOT).as_posix()
            summary = meta["summary"].replace("|", "／")
            page += [f'- [{meta["title"]}]({path.parent.name}/README.md)：{summary}', ""]
            root_lines.append(f'| {slug} | [{meta["title"]}]({relative}) | {summary} | {meta["source_date"]} | {meta["updated"]} |')
        outputs[ROOT / "notes" / slug / "README.md"] = "\n".join(page).rstrip() + "\n"
    outputs[ROOT / "INDEX.md"] = "\n".join(root_lines) + "\n"
    outputs[ROOT / "notes" / "README.md"] = "\n".join(nav) + "\n"
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-index", action="store_true")
    args = parser.parse_args()
    errors = []
    categories = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    slugs = [c["slug"] for c in categories]
    if len(slugs) != len(set(slugs)) or any(not re.fullmatch(r"[a-z][a-z0-9-]*", s) for s in slugs):
        errors.append("catalog.json：分类 slug 重复或格式无效")
    notes = []
    ids = set()
    for category in sorted((ROOT / "notes").iterdir()):
        if not category.is_dir():
            continue
        if category.name not in slugs:
            errors.append(f"未知分类：{category.relative_to(ROOT)}")
            continue
        for folder in sorted(category.iterdir()):
            if not folder.is_dir():
                continue
            entry = folder / "README.md"
            label = folder.relative_to(ROOT).as_posix()
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name):
                errors.append(f"{label}：主题目录须为小写英文/数字及连字符")
            if not entry.is_file() or not (folder / "sources.md").is_file():
                errors.append(f"{label}：缺少 README.md 或 sources.md")
                continue
            try:
                meta = read_metadata(entry)
                missing = REQUIRED - set(meta)
                if missing:
                    raise ValueError(f"缺少字段：{', '.join(sorted(missing))}")
                for key in REQUIRED - {"tags"}:
                    if not isinstance(meta[key], str) or not meta[key].strip():
                        raise ValueError(f"{key} 必须为非空字符串")
                if meta["type"] not in TYPES or meta["status"] not in STATUSES or meta["verification"] not in VERIFICATIONS:
                    raise ValueError("type/status/verification 不在约定范围")
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["id"]):
                    raise ValueError("id 须为小写英文/数字及连字符")
                if meta["id"] in ids:
                    raise ValueError("id 重复")
                ids.add(meta["id"])
                if not isinstance(meta["tags"], list) or not meta["tags"] or any(not isinstance(t, str) or not t.strip() for t in meta["tags"]):
                    raise ValueError("tags 必须为非空字符串数组")
                for key in ("created", "updated", "source_date"):
                    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta[key]):
                        raise ValueError(f"{key} 需要 YYYY-MM-DD")
                    date.fromisoformat(meta[key])
                if meta["updated"] < meta["created"] or meta["source_date"] > meta["updated"]:
                    raise ValueError("日期顺序有误")
                if sum(p.stat().st_size for p in folder.rglob("*") if p.is_file()) > MAX_NOTE:
                    raise ValueError("主题包超过 25 MiB")
                provenance_path = folder / "provenance.json"
                if provenance_path.is_file():
                    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
                    for record in provenance.get("documents", []) + provenance.get("assets", []):
                        destination = (folder / record["destination"]).resolve()
                        if not destination.is_relative_to(folder.resolve()) or not destination.is_file():
                            raise ValueError("迁入清单中的文件缺失或越界")
                        actual = hashlib.sha256(destination.read_bytes()).hexdigest()
                        if actual != record["destination_sha256"]:
                            raise ValueError(f"迁入版本哈希已变化：{record['destination']}；核对改动并更新来源记录")
                notes.append((entry, meta))
            except (ValueError, UnicodeError, KeyError, TypeError) as exc:
                errors.append(f"{label}：{exc}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    for path, content in generated_indexes(categories, notes).items():
        if args.write_index:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        elif not path.is_file() or path.read_text(encoding="utf-8") != content:
            errors.append(f"索引过期：{path.relative_to(ROOT)}；运行 --write-index")
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout.decode("utf-8")
    files = sorted({ROOT / value for value in listing.split("\0") if value})
    total_bytes = 0
    checked_links = 0
    anchor_cache = {}
    for path in files:
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            errors.append(f"禁止符号链接：{relative}")
            continue
        if not path.is_file():
            errors.append(f"Git清单中的文件不存在：{relative}")
            continue
        size = path.stat().st_size
        total_bytes += size
        if size > MAX_FILE:
            errors.append(f"超过单文件 5 MiB：{relative}")
        if path.suffix.lower() in BANNED_EXT or BANNED_DIRS.intersection(relative.parts):
            errors.append(f"不收录的工程资源：{relative}")
        if relative.parts[0] == "notes" and path.suffix.lower() in SOURCE_EXT:
            errors.append(f"工程代码应保留在原项目：{relative}")
        if path.suffix.lower() not in {".md", ".json", ".html", ".css", ".js", ".csv", ".txt", ".svg"}:
            continue
        text = path.read_text(encoding="utf-8-sig")
        if relative.parts[0] == "notes" and LOCAL_PATH.search(text):
            errors.append(f"含本机绝对路径：{relative}")
        if path.suffix.lower() != ".md":
            continue
        for match in LINK.finditer(without_fences(text)):
            raw = match.group(1).strip()
            if raw.startswith("<"):
                raw = raw[1:-1]
            else:
                raw = re.sub(r'\s+["\'][^"\']*["\']$', "", raw)
            target = urlsplit(raw)
            if target.scheme or target.netloc:
                if target.scheme == "file":
                    errors.append(f"本机文件链接：{relative} → {raw}")
                continue
            checked_links += 1
            resolved = (path.parent / unquote(target.path)).resolve() if target.path else path.resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"失效或越界链接：{relative} → {raw}")
                continue
            if target.fragment and resolved.suffix.lower() == ".md":
                if resolved not in anchor_cache:
                    anchor_cache[resolved] = anchors(resolved)
                if unquote(target.fragment) not in anchor_cache[resolved]:
                    errors.append(f"失效锚点：{relative} → {raw}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"检查通过：{len(notes)} 个主题，{len(categories)} 个分类，{len(files)} 个文件，"
          f"{checked_links} 个本地链接，{total_bytes / 1024 / 1024:.2f} MiB。")
    print("范围：元数据、索引、本地链接/锚点与收录边界；未联网核验外链，未重新验证研究结论。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
