---
id: "rl-dexterous-pen-spinning"
title: "灵巧手转笔：LEAP、Revo3 与 Wuji 的阶段实验复盘"
type: "retrospective"
status: "snapshot"
created: "2026-10-22"
updated: "2026-10-22"
source_date: "2026-10-20"
verification: "simulation"
tags: ["rl", "dexterous-hand", "pen-spinning", "leap", "revo3", "wuji", "contact"]
summary: "保留往复转笔和Wuji整圈任务的版本、更正、接触审计及短时诊断，明确长时连续转笔尚未验证。"
---

# 灵巧手转笔：LEAP、Revo3 与 Wuji 的阶段实验复盘

## 范围与版本

本主题于2026-10-22首次建档，原资料截止日期为2026-10-20；各文件的原日期分别保留。收录既有阶段文档或明确标注的提炼摘要，属于历史快照。原作者及具体Agent身份无法可靠确认，不作推定。来源和迁入方式见[sources.md](sources.md)与[provenance.json](provenance.json)。

## 阶段结论

- LEAP/Revo3往复旋转的既定仿真里程碑，不等同于Wuji的整圈换指或真机能力。
- Wuji早期掌心朝下的三手比较已撤回；v7的24/24仅适用于原接触门槛，缩小到真实传感区域会得到不同结果。
- v10/v11选定短时模型在各自固定诊断集通过24/24标准与推力测试；未开封留出集、人工复核和长时任务分别记录。
- v12预检完整两圈为0/24；一次5.5秒整圈不能外推30/60/120秒连续转笔。

## 阅读入口

- [Xense Hand RL 项目总结：从双臂 VLA 到 LEAP / Revo3](report.md)：原文适配快照。
- [历史实验：Wuji Hand 2 掌心朝下场景（对比结论已撤回）](topics/wuji-withdrawn-comparison.md)：原文适配快照。
- [Wuji palm-up pen spinning: v1–v7 results and lessons](topics/wuji-v1-v7-lessons.md)：原文适配快照。
- [Wuji v10 completed robustness screen — 2026-10-20](topics/wuji-v10.md)：原文适配快照。
- [Wuji v11 stronger-push diagnostic — 2026-10-20](topics/wuji-v11.md)：原文适配快照。
- [Wuji v12 duration-bridge preflight — 2026-10-20](topics/wuji-v12-preflight.md)：原文适配快照。

## 已验证与未验证

原报告含仿真训练、CPU/GPU评估、接触分析与用户反馈；本轮仅整理报告。没有重跑或观看全部原始视频。

本轮实际执行文件清单筛选、SHA256捕获、链接/元数据/收录边界检查；这些不构成对原报告的技术复现，也没有重新联网验证外链、价格、厂商规格或论文成绩。原文件保留完整，本文不声称覆盖源目录的后续变化。

## 后续问题

真实指腹接触、自然换指、新版独立人工审阅、连续多圈和真机迁移仍需原工程验证。

## 更新记录

- 2026-10-22：从本机既有资料按明确清单整理，建立入口、来源与哈希追溯；保留原研究日期、失败与未验证事项。
