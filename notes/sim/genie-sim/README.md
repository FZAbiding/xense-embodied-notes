---
id: "sim-genie-sim"
title: "Genie Sim：全身 IK、UMI 回放与仿真工程复盘"
type: "retrospective"
status: "snapshot"
created: "2026-10-19"
updated: "2026-10-19"
source_date: "2026-10-12"
verification: "mixed"
tags: ["sim", "genie-sim", "g2", "whole-body-ik", "umi", "pinocchio", "wbc", "retrospective"]
summary: "整理固定底盘 G2 的 IK 学习、UMI 回放、在线 A/B 与引擎复盘，保留 EEF 撤回、控制长尾及约束失败。"
---

# Genie Sim：全身 IK、UMI 回放与仿真工程复盘

## 范围与版本

收录原工作区 `xense-genie_sim` 中已形成的学习解释、实验总结、修正与过程复盘。主要研究对象是固定底盘 G2 在 Genie Sim 中的双臂、腰部与夹爪联合运动，以及相机、物理引擎和运动学模型的协作。

WBC / UMI 原研究记录覆盖 **2026-10-12 至 2026-10-19**；7 份引擎资料未逐篇明确原研究日期，单独记录为版本快照。捕获的原工程提交为 `5015ce3d4acc61258a0184b1a008a003f67d8a22`，本轮逐文件捕获均与该提交一致。文档中第一人称与“已通过”继承原报告；原执行者的真实身份未独立核实。本轮只整理和迁入文档，来源与许可见 [sources.md](sources.md)，源文件及迁入版哈希见 [provenance.json](provenance.json)。

## 阶段结论

1. **已经形成固定底盘的全身运动学 IK 与仿真位置跟踪链路。** 原报告包含双手目标、腰部锁定/解锁对照、原生关节限位、模型碰撞检查及实际 PhysX 关节反馈；没有完成接触力、平衡和力矩分配的动力学 WBC。
2. **早期 EEF 结果必须按版本阅读。** 虚拟工具框架的初版结果已经撤回其有效性，后续改为模型夹爪指尖中点；再修正相机侧轴、夹爪开合和动态 TCP。历史失败、旧数字与更正都保留。
3. **模型一致性、求解速度和物理跟踪误差是不同证据。** Pinocchio 的离线与在线计算段耗时改善，没有自动消除厘米级反馈 FK 跟踪差；浮点尾数级的模型差异不能当作机器人定位精度。
4. **最新记录仍有明确失败。** 固定首帧的 6 次 A/B 均完成运行，但 002 / URDF 的 HOLD 补充审计发现名义加速度越界；另有制动可行性停止、未执行项及 875.830 ms 控制长周期。平均源 1× 或图像接近 30 fps，不能替代完整约束与长尾验收。
5. **“软直腰”旧命名不能视为手臂严格优先。** 最新核查区分抑制侧倾、前后俯仰和首帧冗余解；固定腰的首帧候选仅经过只读模型检查，尚未验证就位路径和整段执行。

## 阅读导航

建议先看 [阶段、修正与证据导航](report.md)，再按问题阅读：

| 问题 | 入口 |
|---|---|
| 从 FK / IK 学到全身控制，怎样理解数值与误差 | [全身 IK 入门](topics/wbc/WHOLE_BODY_IK_GUIDE_ZH.md)、[图解 IK 教程](topics/umi-replay/IK_LEARNING_GUIDE_ZH.md) |
| UMI 的世界系、旋转表示与 EEF 怎样映射 | [坐标契约](topics/umi-replay/COORDINATES_ZH.md)、[UMI 学习与工作记录](topics/umi-replay/UMI_REPLAY_GUIDE_ZH.md) |
| 历史错误如何修正 | [夹爪 EEF 更正](topics/umi-replay/GRIPPER_EEF_CORRECTION_ZH.md)、[反馈核查](topics/umi-replay/USER_FEEDBACK_REVIEW_ZH.md)、[开合与 Web 修复](topics/umi-replay/GRIPPER_AND_WEB_FIX_ZH.md) |
| Pinocchio 究竟替换哪一层 | [离线模型研究](topics/umi-replay/PINOCCHIO_STUDY_ZH.md)、[在线 A/B 与失败](topics/umi-replay/ONLINE_AB_RESULTS_ZH.md) |
| 为什么卡顿、为什么后仰、手臂优先还缺什么 | [最新回放与腰臂分析](topics/umi-replay/PLAYBACK_ALIGNMENT_AND_WAIST_ZH.md) |
| 引擎、USD 资源与渲染同步的工程经验 | [引擎工程复盘](topics/engine-review.md) |
| 看实际仿真与诊断图 | [2026-10-19 精选回放](assets/episode-000-v6/README.md)、[A/B 图](assets/online-ab-v1/README.md)、[卡顿与腰姿诊断](assets/playback-waist-v1/README.md) |

## 已验证与未验证

原记录的证据包括资料审阅、离线计算、仿真反馈与浏览器操作；具体日期、范围、失败和测试数量以各历史文档为准。仿真中的“实测 EEF”主要是反馈关节状态经过 URDF FK 得到的位姿，未经过外部测量确认。源文件哈希证明文档身份，不能替代原始日志和技术复验。

**2026-10-19 本轮迁入**执行文件筛选、快照与哈希比对、链接修复、敏感路径与账号清理、来源登记及知识库检查。没有重跑仿真、在线 A/B、模型计算或浏览器交互，没有连接真机，没有重新核验外网来源。模型、源码、数据集、环境和原始运行日志仍在原工程；本包保存 23 份主文档、11 份媒体说明、1 篇引擎摘编，以及 32 项精选媒体。

## 后续问题

- 定位控制长尾，验证 HOLD / 暂停 / 恢复的速度状态连续性与离散制动裕量。
- 在同一任务与原生约束下验证合理首帧及明确的腰臂优先级，保留不能完成的目标。
- 明确目标、反馈和已应用命令的时序，再评估实测状态驱动的笛卡尔闭环。
- 增加完整轨迹、无文件前瞻输入和接触任务验证；轮式运动或动力学 WBC 属后续阶段。

## 更新记录

- 2026-10-19：首次建档，捕获截至 `5015ce3` 的阶段文档与精选素材；保留历史撤回、失败及未完成项，补充导航、来源与迁入哈希。原调研日期未改为迁入日期。
