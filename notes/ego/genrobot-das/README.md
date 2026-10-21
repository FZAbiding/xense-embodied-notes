---
id: "ego-genrobot-das"
title: "GenRobot DAS：Ego、手部设备与训练数据调研"
type: "survey"
status: "snapshot"
created: "2026-10-22"
updated: "2026-10-22"
source_date: "2026-09-18"
verification: "source-review"
tags: ["ego", "das", "genrobot", "umi", "data-pipeline"]
summary: "区分DAS Ego/Fingers/Gripper/Dex/Controller的产品与数据用途，保留后处理、工位和验收问题。"
---

# GenRobot DAS：Ego、手部设备与训练数据调研

## 范围与版本

本主题于2026-10-22首次建档，原资料截止日期为2026-09-18；各文件的原日期分别保留。收录既有阶段文档或明确标注的提炼摘要，属于历史快照。原作者及具体Agent身份无法可靠确认，不作推定。来源和迁入方式见[sources.md](sources.md)与[provenance.json](provenance.json)。

## 阶段结论

- 同一产品家族中的 Ego 视频、手部姿态、UMI 示教和执行控制设备并非同一种数据来源。
- Ego 视频与人体动作不自动成为机器人 action；需要标定、坐标、重定向、时间与质量处理。
- 本地转换器审阅仅说明对应版本的数据处理逻辑，不证明厂商精度或完整采集工厂能力。

## 阅读入口

- [简智 GenRobot DAS 具身数据采集设备调研报告](report.md)：原文适配快照。

## 已验证与未验证

原文是公开资料桌面调研和明确标注的本地工程审阅；没有完成真机验收或采购验证。

本轮实际执行文件清单筛选、SHA256捕获、链接/元数据/收录边界检查；这些不构成对原报告的技术复现，也没有重新联网验证外链、价格、厂商规格或论文成绩。原文件保留完整，本文不声称覆盖源目录的后续变化。

## 后续问题

定位真值、同步口径、Dex 完整数据契约和多工位产能仍缺独立验证。

## 更新记录

- 2026-10-22：从本机既有资料按明确清单整理，建立入口、来源与哈希追溯；保留原研究日期、失败与未验证事项。
