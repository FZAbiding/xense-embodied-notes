# IK 学习配图与旧 v5 日志诊断

> 历史文档快照：2026-10-19 迁入。正文中的“本次／我／已通过”沿用原报告口径，不表示本轮重跑；原执行者身份未独立核实。 [阶段与修正导航](../../report.md) · [来源及未随文资源](../../sources.md)。
> 正文命令及 `wbc_demo/`、`logs/` 等路径属于原工程；需在原工程及原环境使用，知识库仅保存笔记与精选素材。
> 素材删选提示：本包保留下方明确列出的文件；原 HTML 导出、原始 JSON/CSV 与其余视频未迁入，原文中的“同目录完整验收包”只描述原工作区。

完整教程：[IK_LEARNING_GUIDE_ZH.md](../../topics/umi-replay/IK_LEARNING_GUIDE_ZH.md)。精选配图见本页末尾。

- `01`：二连杆 FK、Jacobian 与两支解析解；`02`：数值迭代；`03`：v5 职责链；`05`：误差向量分解。均为教学示意，不是机器人新实验。
- `04`：从旧 v5 `umi-realtime-web-reliable-01/run-001` 原始日志重算的曲线；无新机器人运动，不改历史验收指标。
- `metrics.json`：二连杆实际计算结果、v5 统计与输入 SHA256。速度贴近限值占比 0%，加速度贴近限值占比 23.52%；贴边不等于完成误差因果归因。
- 图由 `umi_replay.learning_materials` 生成，中文字体 Noto CJK；无 AI 生成“实验截图”。原 Pinocchio 基准图与 v5 真视频通过相对链接引用，不复制大视频。
- 没有完成 Pinocchio 在线 A/B、实测状态闭环升级或新的力矩 WBC 实验。

生成/复跑命令见教程第 15 节，输出目录必须不存在。


## 本次实际保留的素材

- [01-fk-ik-jacobian.png](01-fk-ik-jacobian.png)
- [02-numerical-iteration.png](02-numerical-iteration.png)
- [03-v5-control-stack.png](03-v5-control-stack.png)
- [04-v5-tracking-diagnostics.png](04-v5-tracking-diagnostics.png)
- [05-error-decomposition.png](05-error-decomposition.png)
