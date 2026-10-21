# 来源、版本与迁入边界

## 原研究与本轮整理

迁入日期：2026-10-22；迁入版本：`local-document-collection-2026-10-22-v1`。下表路径是相对用户资料目录的**逻辑定位文字**，不是本仓库附件链接。原文与目标SHA256见[provenance.json](provenance.json)。源文件只读捕获、复制或提炼，原件未移动或修改；捕获哈希不代表后来修改已经同步。

原作者、具体Agent身份及原文统一许可证无法可靠确认。本轮不补写作者、不代授第三方许可，也不把原报告中的“本轮通过”变成本次已执行测试。`workspace/`仅表示脱敏后的原工作区逻辑位置，示例命令不是本知识库的可运行入口。

| 源文件逻辑定位 | 原记录日期 | 随文目标 | 处理方式 |
|---|---|---|---|
| `src/microduck_rl/docs/microduck_jump_v1_v8_report.md` | 2026-09-14 | [topics/v1-v8.md](topics/v1-v8.md) | 复制正文，适配阅读链接与历史边界 |
| `src/microduck_rl/docs/microduck_jump_v9_report.md` | 2026-10-11 | [report.md](report.md) | 复制正文，适配阅读链接与历史边界 |
| `src/microduck_rl/docs/microduck_jump_v9_landing_recovery.md` | 2026-10-11 | [topics/v9-landing-recovery.md](topics/v9-landing-recovery.md) | 复制正文，适配阅读链接与历史边界 |
| `src/microduck_rl/docs/microduck_mamba_setup_report.md` | 2026-09-05 | [topics/environment-smoke.md](topics/environment-smoke.md) | 提炼摘要，不原样导入工程/页面 |

## 一手依据与版本

下列入口沿用原报告，完整逐条引用及已知固定提交保留在正文；浮动链接不是固定快照。仅本轮归档，没有重新访问。

- [原报告来源入口 1](https://huggingface.co/pollen-robotics/microduck-policies/tree/main)

原研究执行过 MuJoCo/BAM、GPU训练、离线评估与导出检查；这些是继承的历史记录。本轮未训练、加载权重或运行仿真。

V9训练报告与之后的落地恢复记录是两个时间片；后者补充高度不足拆分、303 passed / 1 skipped等原检查结果、候选被拒绝及220/4000 update预算。不能继续把前一个报告的165 update或旧测试失败当作后一个时间片的最终状态；这些均未在本轮重跑。

## 素材与未收录资源

本主题没有随文复制独立图像、视频或可执行演示；正文中的文本示意/公式沿用原文或标记为教学整理。

原始CAD、URDF/mesh、源码、模型/权重、数据集、运行环境、训练日志、完整逐步轨迹及重复PDF/HTML导出不收录。引用它们仅用于说明原证据身份，不声称读者能在本仓库下载或独立复算。

## 未随文保存的工作区引用

以下逐项对应原报告的本地链接。文件名仅说明原依赖；本轮没有加载这些权重或执行脚本，原件的当前可用性和技术内容未逐一重新验证。

<a id="workspace-60514f3ec809"></a>

- 工作区资料：`src/microduck_rl/docs/microduck_jump_policy.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-379d396bd4ae"></a>

- 工作区资料：`src/microduck_rl/docs/microduck_jump_v3.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-9f58407d15e5"></a>

- 工作区资料：`src/microduck_rl/docs/microduck_jump_v9_execution.md`。未随文保存；需要原始证据时回原工作区获取。

<a id="workspace-29505cd328f3"></a>

- 工作区资料：`src/microduck_rl/docs/microduck_jump_v9_plan.md`。未随文保存；需要原始证据时回原工作区获取。

本轮另将原示例的本机临时输出路径改为相对位置，或用工作区临时区逻辑名称说明；不改变原技术结论，源/目标哈希分开保存。
