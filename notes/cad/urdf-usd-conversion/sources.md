# 来源、版本与迁入边界

## 原研究与本轮整理

迁入日期：2026-10-22；迁入版本：`local-document-collection-2026-10-22-v1`。下表路径是相对用户资料目录的**逻辑定位文字**，不是本仓库附件链接。原文与目标SHA256见[provenance.json](provenance.json)。源文件只读捕获、复制或提炼，原件未移动或修改；捕获哈希不代表后来修改已经同步。

原作者、具体Agent身份及原文统一许可证无法可靠确认。本轮不补写作者、不代授第三方许可，也不把原报告中的“本轮通过”变成本次已执行测试。`workspace/`仅表示脱敏后的原工作区逻辑位置，示例命令不是本知识库的可运行入口。

| 源文件逻辑定位 | 原记录日期 | 随文目标 | 处理方式 |
|---|---|---|---|
| `src/xense-description/docs/USD_CONVERSION_FEASIBILITY.md` | 2026-10-15 | [report.md](report.md) | 复制正文，适配阅读链接与历史边界 |
| `src/xense-description/docs/USD_ASSET_AUDIT_AND_ROADMAP.md` | 2026-10-15 | [topics/usd-source-audit.md](topics/usd-source-audit.md) | 复制正文，适配阅读链接与历史边界 |

## 一手依据与版本

下列入口沿用原报告，完整逐条引用及已知固定提交保留在正文；浮动链接不是固定快照。仅本轮归档，没有重新访问。

- [原报告来源入口 1](https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/import_urdf.html)
- [原报告来源入口 2](https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.sim.converters.html)
- [原报告来源入口 3](https://developer.nvidia.com/omniverse)
- [原报告来源入口 4](https://franka.de/models-and-simulation)
- [原报告来源入口 5](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/158f87317fcaa35a7d1706ef364e324d3565939e/usd/RS-rebot-dev-arm/docs/VALIDATION_SKILL.md)
- [原报告来源入口 6](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/README.md)

原研究执行文件来源、OpenUSD解析和数值比较，没有运行Isaac/PhysX/Newton或硬件标定；本轮仅归档。

## 素材与未收录资源

本主题没有随文复制独立图像、视频或可执行演示；正文中的文本示意/公式沿用原文或标记为教学整理。

原始CAD、URDF/mesh、源码、模型/权重、数据集、运行环境、训练日志、完整逐步轨迹及重复PDF/HTML导出不收录。引用它们仅用于说明原证据身份，不声称读者能在本仓库下载或独立复算。

## 未随文保存的工作区引用

以下逐项对应原报告的本地链接。文件名仅说明原依赖；本轮没有加载这些权重或执行脚本，原件的当前可用性和技术内容未逐一重新验证。

<a id="workspace-158fd289bedd"></a>

- 工作区资料：`src/xense-description/docs/ELITE_ACONE_USD_CONVERSION.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-404ddbc1d75b"></a>

- 工作区资料：`src/xense-description/docs/OFFICIAL_USD_IMPORT.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-709b0570c64c"></a>

- 工作区资料：`src/xense-description/reports/elite_acone_usd_validation.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-a4f6f1b2e0ef"></a>

- 工作区资料：`src/xense-description/reports/franka_fr3_official_comparison.json`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-2e928425b247"></a>

- 工作区资料：`src/xense-description/reports/usd_asset_audit_2026-10-15.json`。未随文保存；需要原始证据时回原工作区获取。

本轮另将原示例的本机临时输出路径改为相对位置，或用工作区临时区逻辑名称说明；不改变原技术结论，源/目标哈希分开保存。
