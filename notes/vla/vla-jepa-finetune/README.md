---
id: "vla-vla-jepa-finetune"
title: "VLA-JEPA：微调配方失误与 delta TCP 动作契约"
type: "retrospective"
status: "snapshot"
created: "2026-10-22"
updated: "2026-10-22"
source_date: "2026-07-03"
verification: "source-review"
tags: ["vla", "vla-jepa", "finetuning", "tcp", "action-representation"]
summary: "提炼错误训练入口和未保存checkpoint的教训，说明20D绝对TCP与14D增量动作的参考系、积分和兼容边界。"
---

# VLA-JEPA：微调配方失误与 delta TCP 动作契约

## 范围与版本

本主题于2026-10-22首次建档，原资料截止日期为2026-07-03；各文件的原日期分别保留。收录既有阶段文档或明确标注的提炼摘要，属于历史快照。原作者及具体Agent身份无法可靠确认，不作推定。来源和迁入方式见[sources.md](sources.md)与[provenance.json](provenance.json)。

## 阶段结论

- 原25k计划在13,130步中止且未保存可用checkpoint，不能算有效微调或可恢复训练成果。
- 原修正计划使用同一机器人batch计算action与world-model损失；不把后续计划写成已完成。
- 14D delta TCP使用world平移差与TCP局部相对旋转，夹爪仍为绝对值；兼容名称不等于EEF外参转换。

## 阅读入口

- [VLA-JEPA：微调阶段和 delta TCP 数据契约复盘](report.md)：提炼摘要。

## 已验证与未验证

依据两份本地文档整理实现说明与失败记录，没有复查当前源码或执行训练、推理和机器人实验。

本轮实际执行文件清单筛选、SHA256捕获、链接/元数据/收录边界检查；这些不构成对原报告的技术复现，也没有重新联网验证外链、价格、厂商规格或论文成绩。原文件保留完整，本文不声称覆盖源目录的后续变化。

## 后续问题

修正配方实际完成情况、完整预训练加载、动作往返转换及真机性能需回原工程另验。

## 更新记录

- 2026-10-22：从本机既有资料按明确清单整理，建立入口、来源与哈希追溯；保留原研究日期、失败与未验证事项。
