---
id: "rl-microduck-jump"
title: "Microduck Jump：V1–V9 奖励、恢复与验收复盘"
type: "retrospective"
status: "snapshot"
created: "2026-10-22"
updated: "2026-10-22"
source_date: "2026-10-11"
verification: "mixed"
tags: ["rl", "microduck", "ppo", "jump", "recovery", "evaluation"]
summary: "保留跳跃策略历代失败、V9恢复诊断和严格协议差异；CPU三跳状态完成仍未通过位置质量验收。"
---

# Microduck Jump：V1–V9 奖励、恢复与验收复盘

## 范围与版本

本主题于2026-10-22首次建档，原资料截止日期为2026-10-11；各文件的原日期分别保留。收录既有阶段文档或明确标注的提炼摘要，属于历史快照。原作者及具体Agent身份无法可靠确认，不作推定。来源和迁入方式见[sources.md](sources.md)与[provenance.json](provenance.json)。

## 阶段结论

- V1–V9 的训练内成功、固定协议评估和最终验收分开记录，跨版本成功率不能直接横比。
- V9 A6425 同协议 seed123、各100回合的单跳/三跳为22%/13%；后续恢复候选为29%/7%，未晋升。
- 后续候选在一条CPU轨迹中完成三次状态机，但末段漂移8.66 cm超过1 cm要求；留出恢复仅提升2个百分点，未达到5个百分点门槛。

## 阅读入口

- [Microduck Jump V1–V8 策略、奖励与训练结果报告](topics/v1-v8.md)：原文适配快照。
- [Microduck Jump V9 策略、奖励与训练结果报告](report.md)：原文适配快照。
- [Jump V9：真实落地恢复诊断与小试](topics/v9-landing-recovery.md)：原文适配快照。
- [Microduck：工程闭环冒烟检查的证据边界](topics/environment-smoke.md)：提炼摘要。

## 已验证与未验证

原研究执行过 MuJoCo/BAM、GPU训练、离线评估与导出检查；这些是继承的历史记录。本轮未训练、加载权重或运行仿真。

本轮实际执行文件清单筛选、SHA256捕获、链接/元数据/收录边界检查；这些不构成对原报告的技术复现，也没有重新联网验证外链、价格、厂商规格或论文成绩。原文件保留完整，本文不声称覆盖源目录的后续变化。

## 后续问题

高度裕量、连续请求、位置恢复、多seed最终验收和实机部署仍未解决；没有通过最终端到端交付。

## 更新记录

- 2026-10-22：从本机既有资料按明确清单整理，建立入口、来源与哈希追溯；保留原研究日期、失败与未验证事项。
