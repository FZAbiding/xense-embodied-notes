# 来源、版本与迁入边界

## 原研究与本轮整理

迁入日期：2026-10-22；迁入版本：`local-document-collection-2026-10-22-v1`。下表路径是相对用户资料目录的**逻辑定位文字**，不是本仓库附件链接。原文与目标SHA256见[provenance.json](provenance.json)。源文件只读捕获、复制或提炼，原件未移动或修改；捕获哈希不代表后来修改已经同步。

原作者、具体Agent身份及原文统一许可证无法可靠确认。本轮不补写作者、不代授第三方许可，也不把原报告中的“本轮通过”变成本次已执行测试。`workspace/`仅表示脱敏后的原工作区逻辑位置，示例命令不是本知识库的可运行入口。

| 源文件逻辑定位 | 原记录日期 | 随文目标 | 处理方式 |
|---|---|---|---|
| `src/manus-research/MANUS Metagloves Pro Haptic 数采手套技术、机械结构与产品竞争力调研.md` | 2026-09-21 | [report.md](report.md) | 复制正文，适配阅读链接与历史边界 |
| `src/lerobot-xensehand/docs/manus_ego_wuji_retargeting_analysis.md` | 2026-09-18 | [topics/manus-mint-retargeting.md](topics/manus-mint-retargeting.md) | 提炼学习摘要，不导入内部实现与标定配置 |

## 一手依据与版本

下列入口沿用原报告，完整逐条引用及已知固定提交保留在正文；浮动链接不是固定快照。仅本轮归档，没有重新访问。

- [原报告来源入口 1](https://www.manus-meta.com/products/metagloves-pro-haptic-specs)
- [原报告来源入口 2](https://www.manus-meta.com/blog/manus-quantum-metagloves-reach-end-of-life)
- [原报告来源入口 3](https://www.manus-meta.com/products/metagloves-pro-haptic)
- [原报告来源入口 4](https://doi.org/10.3390/bios15100640)
- [原报告来源入口 5](https://patents.google.com/patent/WO2023037289A1/en)
- [原报告来源入口 6](https://docs.manus-meta.com/3.2.0/Plugins/SDK/C%2B%2B/SDK%20Client/)

原文继承官方文档、产品册、论文、专利及本地工程审阅的证据范围；没有在本轮执行手套或机器人测试。

## 素材与未收录资源

| 素材 | 来源与处理 | 许可与边界 |
|---|---|---|
| [manus-spec-comparison.jpeg](assets/manus-spec-comparison.jpeg) | `src/manus-research/mamus.jpeg`；原工作区的规格对照截图，字节不变 | 原始发布URL、截图作者和具体许可未确认；不由本仓库新增授权，不当作当前规格 |

原始CAD、URDF/mesh、源码、模型/权重、数据集、运行环境、训练日志、完整逐步轨迹及重复PDF/HTML导出不收录。引用它们仅用于说明原证据身份，不声称读者能在本仓库下载或独立复算。

## 未随文保存的工作区引用

以下逐项对应原报告的本地链接。文件名仅说明原依赖；本轮没有加载这些权重或执行脚本，原件的当前可用性和技术内容未逐一重新验证。

<a id="workspace-83694fe727a3"></a>

- 工作区资料：`src/lerobot-xensehand/docs/manus_control.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-e67c444b1cf0"></a>

- 工作区资料：`src/lerobot-xensehand/docs/manus_ego_wuji_retargeting_analysis.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-dfc417ad82a6"></a>

- 工作区资料：`src/lerobot-xensehand/docs/manus_wuji_control.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-83a69876ed5d"></a>

- 工作区资料：`src/manus-research/2602-Manus-全系列产品手册-ProductPortfolio_25-02-2026.pdf`。未随文保存；需要原始证据时回原工作区获取。

重定向源报告中的旧相对链接来自原目录布局；本轮根据实际文件位置修正上述逻辑定位。完整原文仍未随文保存，只有[通用学习摘要](topics/manus-mint-retargeting.md)。原审阅没有展开SDK/优化器子模块或执行设备测试。
