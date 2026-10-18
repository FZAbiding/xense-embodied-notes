# 来源索引与证据边界

> 本页继承 2026-09-22 原研究的来源记录；2026-10-18 仅调整知识库归档与素材引用，未重新验证技术结论。

检索日期：2026-09-22。正文中的链接就近支持对应陈述。厂家规格均按官方声明引用，不作为独立实测；机械、热和成本分析另标工程推断。网页与下载端点会变化，读者复核时应同时核对版本。

## 1. BrainCo Revo 3

| 编号 | 一手资料 | 用途与限制 |
| --- | --- | --- |
| R1 | [正式产品手册](https://www.brainco-hz.com/docs/revolimb-hand/revo3/parameters.html) | 型号、自由度、外形、触觉配置、供电、通信与安全注意事项 |
| R2 | [正式通信协议](https://www.brainco-hz.com/docs/revolimb-hand/revo3/protocol.html) | 寄存器、电气量单位、数据分组、状态与保护；不是 FOC 源码 |
| R3 | [REVO3_MOTOR_API](https://github.com/BrainCoTech/brainco-revo3-sdk/blob/main/docs/device/REVO3_MOTOR_API.md) | mA 而非标定 N·m 的明确说明；SKU 成熟度与关节顺序 |
| R4 | [SDK 仓库](https://github.com/BrainCoTech/brainco-revo3-sdk) | 可用接口、发布包和集成文档，开放程度需按组件分别判断 |
| R5 | [官方模型库](https://github.com/BrainCoTech/brainco-description) | 输出运动链与仿真元数据，不能反推电机转子轴或真实扭矩 |
| R6 | [CN121625194A](https://patents.google.com/patent/CN121625194A/zh) | 强脑模块化电路申请；申请日 2026-02-04，公开日 2026-03-10；不是现售产品逐项结构确认 |
| R7 | [staging 产品页](https://staging.brainco.tech/product/revo3) | 仅用于记录历史/并行版本口径，优先级低于正式手册 |
| R8 | [BrainCo 官方代码组织](https://github.com/BrainCoTech) | 学习、重定向、ROS 与模型生态入口，不代表所有项目生产就绪 |

URDF 审核固定到提交 `f332a6f0dc944e26b82976b637074b03f7ee8a2c`，文件 `revo3_system/urdf/revo3_right.urdf`。结果见 [模型审阅摘要](sources.md#model-audit-summary)。

## 2. Sharpa Wave

| 编号 | 一手资料 | 用途与限制 |
| --- | --- | --- |
| S1 | [Wave / Wave SE 产品页](https://www.sharpa.com/pages/wave) | 需读取图片标题区分两个型号；并非所有指标都有完整测试条件 |
| S2 | [官方文档入口](https://www.sharpa.com/pages/documentation) | 嵌入在线文档；内容入口为 [sharpa-docs](https://sharpa-robotics.github.io/sharpa-docs/) |
| S3 | [Wave 官方 PDF](https://documentationpdf.sharpa.com/api/pdf/wave) | 本次取得 175 页；动态生成端点，未来页码/内容可能改变 |
| S4 | [官方 URDF/USD/XML](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml) | 核对运动链、文件版本与模型参数，不是制造图 |
| S5 | [MuJoCo Menagerie 模型说明](https://github.com/google-deepmind/mujoco_menagerie/blob/main/sharpa_wave/README.md) | 原始模型转换者的说明；辅助核对 5+4+4+4+5 的拓扑 |
| S6 | [SDK 分发仓库](https://github.com/sharpa-robotics/sharpa-wave-sdk) | SDK 库文件、头文件和安装入口；不代表电机固件开源 |
| S7 | [固件分发仓库](https://github.com/sharpa-robotics/sharpa-wave-firmware) | 升级包分发与固件源码不是同一概念 |
| S8 | [OpenCAD 库](https://github.com/sharpa-robotics/sharpa-opencad-library) | 区分安装附件/简化模型与内部制造级 CAD |
| S9 | [ADEPT 论文](https://arxiv.org/abs/2608.19182) | 2026-08-19 提交，Flexiv–Sharpa 研究系统；不是 Revo/Wave 对照试验 |

URDF 审核固定到提交 `0d19cac602f46456b819e4b6a2c09a74982c9a3e`，文件 `wave_01/right_sharpa_wave/right_sharpa_wave.urdf`。

PDF 重点定位：第 8 页电气与性能；第 9 页关节范围；第 11 页根部力矩传感；第 11–12 页附近的触觉/环境规格；第 14 页二维关节工作空间；第 28–30 页反馈与控制模式；第 96 页 MIT 公式。少数跨页表格排版以实际页面为准。

## 3. 本次处理的主要冲突

| 冲突 | 本报告处理 |
| --- | --- |
| Revo 压阻点数 416/301 与 451/336 | 当日正式手册采用 451、336；保留旧口径提示，不混算 |
| Revo 有 VT 产品表，但 SDK 标 Hardware Pilot | 两条同时保留，要求以交付清单与设备信息确认 |
| Wave 产品页有两列但文本抓取缺型号标题 | 下载并检查标题图片，确认第二列为 Wave SE |
| Wave 官网 ±20° 侧摆，手册一般轴范围 ±18° 且组合范围受限 | 规划时优先使用对应手册/固件限位与二维工作空间，不用官网单数值矩形化 |
| Wave 官网 180 fps，手册区分标准/高性能模式与延迟 | 不把图像峰值帧率推广成所有处理输出的同步刷新率 |
| Wave 官网页面把 N 单位写在空间分辨率行 | 以手册区分 20 mN 力分辨率与 1 mm 空间分辨率 |
| URDF 质量与实物规格不一致或缺实物数据 | URDF 仅作模型审核，不代替秤重或官方实物重量 |

## 已从原材料确认的固定提交

| 仓库 | 提交 |
|---|---|
| [BrainCoTech/brainco-description](https://github.com/BrainCoTech/brainco-description) | [f332a6f0dc944e26b82976b637074b03f7ee8a2c](https://github.com/BrainCoTech/brainco-description/tree/f332a6f0dc944e26b82976b637074b03f7ee8a2c) |
| [sharpa-robotics/sharpa-urdf-usd-xml](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml) | [0d19cac602f46456b819e4b6a2c09a74982c9a3e](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/tree/0d19cac602f46456b819e4b6a2c09a74982c9a3e) |

其他未保存提交信息的链接保留原地址，不伪造 revision。

<a id="model-audit-summary"></a>

## 原模型审阅摘要

下表摘自原工作区的 `sources/model_audit.json`，完整关节数组及原模型仍留在原工程。模型质量与运动链仅为文件事实，不能代替硬件规格或实测。

| 对象 | 非固定关节数 | 模型质量 / kg | 固定版本模型 |
|---|---:|---:|---|
| Revo 3 | 21 | 1.105 | [原模型](https://raw.githubusercontent.com/BrainCoTech/brainco-description/f332a6f0dc944e26b82976b637074b03f7ee8a2c/revo3_system/urdf/revo3_right.urdf) |
| Sharpa Wave | 22 | 1.2432649999999998 | [原模型](https://raw.githubusercontent.com/sharpa-robotics/sharpa-urdf-usd-xml/0d19cac602f46456b819e4b6a2c09a74982c9a3e/wave_01/right_sharpa_wave/right_sharpa_wave.urdf) |

本轮未重新解析原模型，也未迁入 URDF/mesh。

<a id="material-sources"></a>

## 素材与数据来源

厂家图片与官方手册通过原始来源链接展示，本仓库没有重新保存这些图片或手册页面；获取它们需要联网。原作者和原始校验值见下表及 `provenance.json`。

| 原素材 | 原权利人 | 官方来源 | 原核验日期 |
|---|---|---|---|
| `revo3_dof.png` | BrainCo | [原始来源](https://www.brainco-hz.com/docs/revolimb-hand/images/revo3_dof_distribution.png) | 2026-09-22 |
| `revo3_product.png` | BrainCo | [原始来源](https://www.brainco-hz.com/docs/revolimb-hand/images/revo3_rendering.png) | 2026-09-22 |
| `sharpa_second_column_label.png` | Sharpa | [原始来源](https://www.sharpa.com/cdn/shop/files/20260818-171150.png?v=1787044335&width=600) | 2026-09-22 |
| `sharpa_wave_product.jpg` | Sharpa | [原始来源](https://www.sharpa.com/cdn/shop/files/Codex_2026_8_17_17_57_19.jpg?v=1787034361&width=1200) | 2026-09-22 |
| `sharpa_workspace_manual_p14.png` | Sharpa | [原始来源](https://documentationpdf.sharpa.com/api/pdf/wave) | 2026-09-22 |

随文自绘图/表：

| 文件 | 生成方式与边界 |
|---|---|
| [01_kinematic_topology.png](assets/diagrams/01_kinematic_topology.png) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [01_kinematic_topology.svg](assets/diagrams/01_kinematic_topology.svg) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [02_control_sensing.png](assets/diagrams/02_control_sensing.png) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [02_control_sensing.svg](assets/diagrams/02_control_sensing.svg) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |

原研究为 Agent 辅助成果，具体 Agent 模型/署名未能可靠确认；未推定第三方素材的再发布许可。自绘图表的原创部分沿用本仓库尚待选择的许可状态，不代替原始参考资料条款。

## 归档边界

原研究逻辑位置：`src/wuji-research/revo3-vs-sharpa`。本轮只迁入阶段报告、自绘图表、小型参数表和来源记录；原 CAD、教学模型、SDK、源码、下载和运行环境继续留在原工程。

[provenance.json](provenance.json) 记录源文件、原文哈希、归档版本及外部素材身份。原报告与素材未被本轮修改。
