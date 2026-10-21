# 来源、版本与迁入边界

## 原研究与本轮整理

迁入日期：2026-10-22；迁入版本：`local-document-collection-2026-10-22-v1`。下表路径是相对用户资料目录的**逻辑定位文字**，不是本仓库附件链接。原文与目标SHA256见[provenance.json](provenance.json)。源文件只读捕获、复制或提炼，原件未移动或修改；捕获哈希不代表后来修改已经同步。

原作者、具体Agent身份及原文统一许可证无法可靠确认。本轮不补写作者、不代授第三方许可，也不把原报告中的“本轮通过”变成本次已执行测试。`workspace/`仅表示脱敏后的原工作区逻辑位置，示例命令不是本知识库的可运行入口。

| 源文件逻辑定位 | 原记录日期 | 随文目标 | 处理方式 |
|---|---|---|---|
| `src/php_parkour/PHP_HUMANOID_LOCOMOTION_BEGINNER_GUIDE.md` | 未知；由2026-10-20总览引用 | [report.md](report.md) | 提炼摘要，不原样导入工程/页面 |
| `src/php_parkour/PHP_PARKOUR_PROJECT_GUIDE.md` | 2026-10-20 | [report.md](report.md) | 提炼摘要，不原样导入工程/页面 |
| `src/php_parkour/PHP_REPRODUCTION_GUIDE.md` | 2026-10-15 | [report.md](report.md) | 提炼摘要，不原样导入工程/页面 |
| `src/php_parkour/reports/phase1_second_block_diagnosis_2026-10-17.md` | 2026-10-17 | [report.md](report.md) | 提炼摘要，不原样导入工程/页面 |
| `src/php_parkour/reports/phase1_second_block_live_trace_2026-10-19.md` | 2026-10-19 | [topics/second-block-trace.md](topics/second-block-trace.md) | 复制正文，适配阅读链接与历史边界 |
| `src/php_parkour/reports/phase1_block_aware_2026-10-19.md` | 2026-10-19 | [topics/block-aware.md](topics/block-aware.md) | 复制正文，适配阅读链接与历史边界 |

## 一手依据与版本

下列入口沿用原报告，完整逐条引用及已知固定提交保留在正文；浮动链接不是固定快照。仅本轮归档，没有重新访问。

- [原报告来源入口 1](https://arxiv.org/html/2602.15827v2)
- [原报告来源入口 2](https://github.com/amazon-far/php_parkour)
- [原报告来源入口 3](https://github.com/amazon-far/php_parkour/releases/tag/student-assets-v1)

原研究记录MuJoCo闭环、深度/动作/接触诊断；本页方法部分为教学提炼。本轮未重跑、未观看全部视频、未重新核实上游。

## 素材与未收录资源

本主题没有随文复制独立图像、视频或可执行演示；正文中的文本示意/公式沿用原文或标记为教学整理。

原始CAD、URDF/mesh、源码、模型/权重、数据集、运行环境、训练日志、完整逐步轨迹及重复PDF/HTML导出不收录。引用它们仅用于说明原证据身份，不声称读者能在本仓库下载或独立复算。

## 未随文保存的工作区引用

以下逐项对应原报告的本地链接。文件名仅说明原依赖；本轮没有加载这些权重或执行脚本，原件的当前可用性和技术内容未逐一重新验证。

<a id="workspace-968553293952"></a>

- 工作区资料：`src/php_parkour/demos/phase1-onnx-block-aware-v1/README.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-ca1d7f93dd51"></a>

- 工作区资料：`src/php_parkour/demos/phase1-onnx-guided-short-v1/README.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-3a3a6e2c7458"></a>

- 工作区资料：`src/php_parkour/demos/phase1-onnx-second-block-trace-v1/README.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-2c37634cea3a"></a>

- 工作区资料：`src/php_parkour/demos/phase1-onnx-second-block-trace-v1/policy_ticks.jsonl`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-f1bc97ff87c0"></a>

- 工作区资料：`src/php_parkour/demos/phase1-onnx-w-only-v4/README.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-3e31188c3f96"></a>

- 工作区资料：`src/php_parkour/reports/phase1_block_aware_diag012.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-ca670ccb838d"></a>

- 工作区资料：`src/php_parkour/reports/phase1_block_aware_diag012.png`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-6d44c53152aa"></a>

- 工作区资料：`src/php_parkour/reports/phase1_block_aware_probe_011_blocked.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-1c6c56f4a75e"></a>

- 工作区资料：`src/php_parkour/reports/phase1_block_aware_probe_013_blocked.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-7ea9c17219e7"></a>

- 工作区资料：`src/php_parkour/reports/phase1_second_block_probe_010.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-e25e0e6f57aa"></a>

- 工作区资料：`src/php_parkour/reports/phase1_second_block_trace_diag010.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-871edbbc3da9"></a>

- 工作区资料：`src/php_parkour/reports/phase1_second_block_trace_diag010.png`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-10c3843a42a8"></a>

- 工作区资料：`src/php_parkour/reports/phase1_short_guard_followup_2026-10-17.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-21e91a7576cd"></a>

- 工作区资料：`src/php_parkour/scripts/php_analyze_second_block.py`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-93746aeedf18"></a>

- 工作区资料：`src/php_parkour/scripts/php_block_guidance.py`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-ba81038612df"></a>

- 工作区资料：`src/php_parkour/scripts/php_diagnostic_integrity.py`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-8085915f2907"></a>

- 工作区资料：`src/php_parkour/scripts/php_official_benchmark.py`。未随文保存；需要原始证据时回原工作区获取。
