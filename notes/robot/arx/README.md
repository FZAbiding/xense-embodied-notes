---
id: "robot-arx"
title: "ARX / Seeed B601-DM：双臂平台研究阶段总结"
type: "survey"
status: "snapshot"
created: "2026-10-16"
updated: "2026-10-16"
source_date: "2026-10-16"
verification: "mixed"
tags: ["robot", "arx", "acone", "seeed", "b601-dm", "dual-arm", "hardware", "control"]
summary: "整理ACOne与B601-DM的结构、控制、臂展、LIFT及防坠急停研究，保留R2布局和R3资料边界。"
---

# ARX / Seeed B601-DM：双臂平台研究阶段总结

## 本阶段范围

原研究对 ARX ACOne/A5/X5、Seeed B601-DM 及 LIFT/LIFT-mini 进行了资料、几何和源码对比。
本次捕获的是 R3 资料版：保留 R2 机械布局，包含防坠与急停增量专题。原研究日期为 2026-10-16，由 Agent 辅助完成。
这次迁入只整理总结、专题和必要预览，不迁入原始 CAD、URDF、源码、代码摘录或运行环境。来源见 [sources.md](sources.md)。

## 先记住的结论

- 原报告认为双 B601-DM 可作为轻载双臂平台的开发起点；几何、控制映射、零位、标定和验收需要按新平台处理。
- 相近外观或同系列电机不足以证明平台等效，臂展比较必须先统一参考点和工具长度。
- 双臂通信、配置值与实际发送值、反馈有效性及故障退出路径需要逐层核对。
- 防坠与急停专题记录的是静态审阅和设计思路，原研究尚未验证对应真机故障根因或硬件方案。

## 阅读入口

- [总报告](report.md)：主要问题、对比结论与实施路线。
- [机械、运动学与 CAD 对比](topics/02_mechanical_comparison.md)。
- [电机、供电、控制器与外围硬件](topics/03_motors_and_electrical.md)。
- [协议、零位、双臂控制与源码核查](topics/04_protocol_and_control.md)。
- [肩宽、基座高度、头部相机与标定设计](topics/05_layout_and_camera_design.md)。
- [实施路线、算法、预算与验收](topics/06_build_and_validation_plan.md)。
- [待实物确认事项与取证表](topics/07_open_questions.md)。
- [双DM与ACOne的J2高度复核](topics/10_J2_height_comparison.md)。
- [R2：与ACOne同宽、同高并集成J1的底座方案](topics/11_acone_aligned_base_r2.md)。
- [LIFT / LIFT-mini官方资源与横向比较](topics/12_lift_resources_and_comparison.md)。
- [ACOne/X5与Seeed B601-DM臂展比较](topics/14_arm_reach_comparison.md)。
- [Seeed B601-DM 防坠、异常下使能与急停设计](topics/15_fall_prevention_and_emergency_stop.md)。
- [来源、固定提交与未随文保存资料](sources.md)。
- [迁入清单与原文哈希](provenance.json)。

## 已验证与未验证

原报告的公开文件核查、几何分析与离线检查继承其原始边界，详细方法和例外仍以对应专题为准。
涉及用户 ACOne 配置的确认只适用于原报告中的特定设备；内部代码证据未迁入本库。
本轮未重新执行原模型/控制验证；制造、真实CAN时序、标定、持续负载、碰撞及防坠急停验收仍不能由本次归档代替。

## 后续学习

在原工程继续完成机械集成、平台适配与实物取证，形成下一阶段总结后按来源版本更新本主题。

## 更新记录

- 2026-10-16：首批迁入，保留原阶段结论与验证边界，整理链接与精选素材。
