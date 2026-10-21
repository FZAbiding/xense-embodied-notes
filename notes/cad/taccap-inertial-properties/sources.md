# 来源、版本与迁入边界

## 原研究与本轮整理

迁入日期：2026-10-22；迁入版本：`local-document-collection-2026-10-22-v1`。下表路径是相对用户资料目录的**逻辑定位文字**，不是本仓库附件链接。原文与目标SHA256见[provenance.json](provenance.json)。源文件只读捕获、复制或提炼，原件未移动或修改；捕获哈希不代表后来修改已经同步。

原作者、具体Agent身份及原文统一许可证无法可靠确认。本轮不补写作者、不代授第三方许可，也不把原报告中的“本轮通过”变成本次已执行测试。`workspace/`仅表示脱敏后的原工作区逻辑位置，示例命令不是本知识库的可运行入口。

| 源文件逻辑定位 | 原记录日期 | 随文目标 | 处理方式 |
|---|---|---|---|
| `Desktop/TacCap主从夹爪_质量质心惯量调研与重构报告_2026-10-12.md` | 2026-10-12 | [report.md](report.md) | 复制正文，适配阅读链接与历史边界 |
| `Desktop/TacCap主夹爪_原始STEP到URDF与物性数据转换步骤_2026-10-12.md` | 2026-10-12 | [topics/master-step-to-urdf.md](topics/master-step-to-urdf.md) | 复制正文，适配阅读链接与历史边界 |
| `Desktop/TacCap从夹爪_STEP到URDF转换与物性获取学习笔记.md` | 2026-10-09 | [topics/slave-step-to-urdf.md](topics/slave-step-to-urdf.md) | 复制正文，适配阅读链接与历史边界 |
| `Desktop/主夹爪与转接件质量属性分离_理论推导与实验流程.md` | 2026-10-10 | [topics/tool-adapter-separation.md](topics/tool-adapter-separation.md) | 复制正文，适配阅读链接与历史边界 |

## 一手依据与版本

下列入口沿用原报告，完整逐条引用及已知固定提交保留在正文；浮动链接不是固定快照。仅本轮归档，没有重新访问。

- [原报告来源入口 1](https://github.com/robotology/icub-models-generator)
- [原报告来源入口 2](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_23dof.urdf)
- [原报告来源入口 3](https://raw.githubusercontent.com/wuji-technology/wuji-description/main/hand2/hand2_beta2/body/urdf/left.urdf)
- [原报告来源入口 4](https://github.com/Wonikrobotics-git/allegro_hand_ros_v5/tree/master-4finger)
- [原报告来源入口 5](https://blog.robotiq.com/hubfs/support-files/TCP_20and_20Center_20of_20Mass_20of_20Robotiq_20Products_20V1.1_20210623.pdf)
- [原报告来源入口 6](https://assets.robotiq.com/website-assets/support_archives/document_en/IMB-311012_20180226.pdf)

原文主要是公开方法调研、本地文件只读分析、公式推导与实施计划；没有完成称量、实物质心/惯量辨识或新模型转换。

## 素材与未收录资源

本主题没有随文复制独立图像、视频或可执行演示；正文中的文本示意/公式沿用原文或标记为教学整理。

原始CAD、URDF/mesh、源码、模型/权重、数据集、运行环境、训练日志、完整逐步轨迹及重复PDF/HTML导出不收录。引用它们仅用于说明原证据身份，不声称读者能在本仓库下载或独立复算。
