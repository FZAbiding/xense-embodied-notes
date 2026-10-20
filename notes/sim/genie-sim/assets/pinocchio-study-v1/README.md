# Pinocchio G2 模型研究 v1

> 历史文档快照：2026-10-19 迁入。正文中的“本次／我／已通过”沿用原报告口径，不表示本轮重跑；原执行者身份未独立核实。 [阶段与修正导航](../../report.md) · [来源及未随文资源](../../sources.md)。
> 正文命令及 `wbc_demo/`、`logs/` 等路径属于原工程；需在原工程及原环境使用，知识库仅保存笔记与精选素材。
> 素材删选提示：本包保留下方明确列出的文件；原 HTML 导出、原始 JSON/CSV 与其余视频未迁入，原文中的“同目录完整验收包”只描述原工作区。

本页保留离线基准图；[metrics.json（工作区资料）](../../sources.md#workspace-materials) 未随文迁入。
这是离线模型兼容性与计算段基准，不是 Pinocchio 整段仿真闭环演示。

- 输入：v5 实际回放 `umi-realtime-web-reliable-01/run-001/joint_trace.csv`，均匀采样 100 个完整反馈状态。
- Pinocchio 4.1.0 运行在独立 logs venv；没有改动 xense-wbc 基础包或默认在线 IK 后端。
- 指尖 EEF、实测从动关节偏差和测试世界变换保持一致，最大 Jacobian 元素差 `2.410e-8`。
- 四项可选模型测试还覆盖同一 QP 的单步命令对照；不能据此宣称实机力控或闭环抗扰已通过。
- `metrics.json` 包含 URDF、实际回放报告和反馈 CSV 的输入 SHA256，原始文件仍在本机 logs，不公开整个数据集。
- 原理、限制和复现命令：[PINOCCHIO_STUDY_ZH.md](../../topics/umi-replay/PINOCCHIO_STUDY_ZH.md)。


## 本次实际保留的素材

- [kinematics-comparison.png](kinematics-comparison.png)
