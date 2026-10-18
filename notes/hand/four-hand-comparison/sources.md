# 来源、版本与证据边界

> 本页继承 2026-09-23 原研究的来源记录；2026-10-18 仅调整知识库归档与素材引用，未重新验证技术结论。

本次整理日期：2026-09-23。沿用旧材料时保留原核验日期，不将新报告日期冒充所有资料的首次获取日期。未开展实机试验，未向厂商提交采购/注册表单。

## 1. Wuji Hand 2

| 来源 | 本次用途 |
| --- | --- |
| [当前产品概览](https://docs.wuji.tech/docs/en/wuji-hand/latest/overview/) | 2.2 Beta 名称、20 轴、尺寸/质量口径、Ethernet 与供电；2026-09-23 核对 |
| [版本兼容](https://docs.wuji.tech/docs/en/wuji-hand/latest/version-compatibility/) | 2.2 对应 hand2_beta2，2.1 对应 hand2_beta1；不能将命名更新误认为额外一代硬件 |
| [控制指南](https://docs.wuji.tech/docs/en/wuji-hand/latest/control-guide/) | effort 单位 A、1 kHz 报文、GET 限频、轴序说明 |
| [SDK Reference](https://docs.wuji.tech/docs/en/wuji-hand/latest/sdk-reference/) | 状态/诊断、订阅、单设备版本与接口 |
| [用户须知](https://docs.wuji.tech/docs/en/wuji-hand/latest/user-notice/) | 热、寿命、外力估算、样机负载承诺等限制；非质量问题发生率 |
| [维护与恢复](https://docs.wuji.tech/docs/en/wuji-hand/latest/troubleshooting/) | 停机后失力、通信故障、排线与维修边界 |
| [固定提交触觉示例](https://github.com/wuji-technology/wuji-sdk/blob/f36a41969d8754ef364a34b59196e4d7e211599f/examples/python/wuji_hand_2/3.fingertip_typed.py) | 40+4×34 点、100 Hz、归一化单位、合力及坐标系；代码说明而非完整计量规格书 |
| [官方模型](https://github.com/wuji-technology/wuji-description) | 可用于运动学/碰撞，不等于内部制造图 |

Wuji SDK 审核提交：`f36a41969d8754ef364a34b59196e4d7e211599f`。旧专题中的单一用户 Hand 1 反馈、渠道指尖峰值和教学 A/B 模型不用于本报告四款的性能排名。

## 2. 临界点 AGILINK OmniHand 3 Ultra-M

| 来源 | 本次用途 |
| --- | --- |
| [当前 Ultra-M 产品页](https://www.agilink-ai.com/ultra-m.html) | 20 轴、630 g、尺寸、3 kg/8 kg、触觉、CAN FD/Ethernet、热与循环声明；2026-09-23 核对 |
| [官方单页规格 PDF](https://www.agilink-ai.com/uploads/upload/files/20260530/a7b12675ce5e3b4e9b913801c0c6f659.pdf) | 与当前页面对照；PDF 是 CAN FD/RS485/EtherCAT 口径；路径日期不作为正式版本发布日期 |
| [SDK 固定提交](https://github.com/AgibotTech/agillink_omnihand_sdk/tree/026740d9fdd8ba32b0605fa702a992b322076f1b) | 型号专属公开头文件、示例、ROS 2 接口，不推断未开放的内部功能 |
| [Ultra-M 头文件](https://github.com/AgibotTech/agillink_omnihand_sdk/blob/026740d9fdd8ba32b0605fa702a992b322076f1b/linux/x64/cpp/include/omnihand/omnihand_3_ultra_m.h) | 20 主动/0 被动、5×4 关节名、XenseFrame/PalmFrame、CAN 与 SoC 通路 |
| [运动学映射头文件](https://github.com/AgibotTech/agillink_omnihand_sdk/blob/026740d9fdd8ba32b0605fa702a992b322076f1b/linux/x64/cpp/include/omnihand/kinematics/omnihand_3_ultra_m/omnihand_3_ultra_m_solver.h) | 关节角到输入码的逐关节线性映射，不能因此推断物理传动比为 1 |
| [ROS 2 型号对照](https://github.com/AgibotTech/agillink_omnihand_sdk/blob/026740d9fdd8ba32b0605fa702a992b322076f1b/doc/en/API_ROS2.md) | H3U_M 的 CSP/PP、通信支持，排除 O10/O12 的其他模式和触觉频率 |
| [SDK v1.1.8](https://github.com/AgibotTech/agillink_omnihand_sdk/releases/tag/v1.1.8) | 可选 Xense 指尖与 SoC 掌面感知支持 |
| [产品矩阵](https://www.agilink-ai.com/) | Ultra-M 与 Ultra-T 并行，不借用整个产品线出货作为 Ultra-M 成熟度证明 |

SDK 审核提交：`026740d9fdd8ba32b0605fa702a992b322076f1b`。头文件含虚函数默认返回/占位内容，不能仅凭接口声明认定特定硬件和动态库已实现所有功能；也不能因为公共基类默认返回 false 就断定实际派生实现不支持。本文对功能的判断以型号文档和实际数据结构为边界，未运行任何硬件命令。

未采用经销商的美元标价、型号首发时间转述，以及媒体“无传动损耗”等不可验证表述；没有把旧 OmniHand Pro 的 12 个主动自由度和 19 个总自由度套给 Ultra-M。

## 3. Sharpa Wave 与 Revo 3：复用范围

原始研究位于 `revo3-vs-sharpa`，2026-09-22 已完成来源与模型核对。原研究曾将所需图片复制进自身包并校验；本知识库版本改用官方图片外链，自绘图表随文保存，详见下方素材说明。

| 来源 | 复用/复核情况 |
| --- | --- |
| [Wave 产品页](https://www.sharpa.com/pages/wave) | 2026-09-23 再次访问；标准 Wave 与 Wave SE 区分；不混表 |
| [Wave 官方 PDF](https://documentationpdf.sharpa.com/api/pdf/wave) | 沿用 2026-09-22 下载的 175 页版本；本次重新检查第 8–12、28–30 页等；动态端点未来可能变化 |
| [Wave 文档入口](https://www.sharpa.com/pages/documentation) | 上述手册的官方入口 |
| [Sharpa 官方模型](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml) | 旧报告固定提交 0d19cac602f46456b819e4b6a2c09a74982c9a3e；本次使用 5/4/4/4/5 拓扑，不采用模型质量作为实物规格 |
| [Revo 产品手册](https://www.brainco-hz.com/docs/revolimb-hand/revo3/parameters.html) | 数值沿用 2026-09-22 正式页面核验；2026-09-23 抓取曾超时，不声称全部规格已当日重新确认 |
| [Revo Motor API](https://github.com/BrainCoTech/brainco-revo3-sdk/blob/main/docs/device/REVO3_MOTOR_API.md) | 2026-09-23 再次核对：mA 语义、无标定 N·m、Ultra VisionTouch 的 Hardware Pilot 状态 |
| [BrainCo 官方模型](https://github.com/BrainCoTech/brainco-description) | 旧报告固定提交 f332a6f0dc944e26b82976b637074b03f7ee8a2c；仅作主动运动链支持 |
| [ADEPT](https://arxiv.org/abs/2608.19182) | 研究系统使用证据，不是四产品对照试验 |

Revo 点数采用旧报告所核验的正式页面 451/336，而不是 staging 的 416/301；VR/视触觉 marker 与压阻采样点不相加做跨产品排名。Wave 手册的高性能模式 180 Hz 明确对应原始图像流，不推广到所有处理输出。

## 已从原材料确认的固定提交

| 仓库 | 提交 |
|---|---|
| [AgibotTech/agillink_omnihand_sdk](https://github.com/AgibotTech/agillink_omnihand_sdk) | [026740d9fdd8ba32b0605fa702a992b322076f1b](https://github.com/AgibotTech/agillink_omnihand_sdk/tree/026740d9fdd8ba32b0605fa702a992b322076f1b) |
| [wuji-technology/wuji-sdk](https://github.com/wuji-technology/wuji-sdk) | [f36a41969d8754ef364a34b59196e4d7e211599f](https://github.com/wuji-technology/wuji-sdk/tree/f36a41969d8754ef364a34b59196e4d7e211599f) |

其他未保存提交信息的链接保留原地址，不伪造 revision。

<a id="material-sources"></a>

## 素材与数据来源

厂家图片与官方手册通过原始来源链接展示，本仓库没有重新保存这些图片或手册页面；获取它们需要联网。原作者和原始校验值见下表及 `provenance.json`。

| 原素材 | 原权利人 | 官方来源 | 原核验日期 |
|---|---|---|---|
| `omnihand_ultra_m.png` | AGILINK | [原始来源](https://www.agilink-ai.com/uploads/upload/images/20260709/7a0a372bd3ddfd2f1fea150e9ea74984.png) | 2026-09-23 |
| `revo3_product.png` | BrainCo | [原始来源](https://www.brainco-hz.com/docs/revolimb-hand/images/revo3_rendering.png) | 2026-09-22 |
| `sharpa_wave_product.jpg` | Sharpa | [原始来源](https://www.sharpa.com/cdn/shop/files/Codex_2026_8_17_17_57_19.jpg?v=1787034361&width=1200) | 2026-09-22 |
| `wuji_structure.png` | WUJI TECH | [原始来源](https://docs.wuji.tech/_next/static/media/structure-white.1f578143.png) | 2026-09-23 |

随文自绘图/表：

| 文件 | 生成方式与边界 |
|---|---|
| [01_structure_mass.png](assets/diagrams/01_structure_mass.png) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [01_structure_mass.svg](assets/diagrams/01_structure_mass.svg) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [02_control_evidence.png](assets/diagrams/02_control_evidence.png) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [02_control_evidence.svg](assets/diagrams/02_control_evidence.svg) | 原研究自绘的分析/教学图，非实物拆解或制造图，本轮未重新绘制 |
| [comparison.csv](assets/tables/comparison.csv) | 原研究整理的参数与来源对照表，保留缺失值和核验日期 |

原研究为 Agent 辅助成果，具体 Agent 模型/署名未能可靠确认；未推定第三方素材的再发布许可。自绘图表的原创部分沿用本仓库尚待选择的许可状态，不代替原始参考资料条款。

## 5. 研究边界

本次没有四款同台的力矩—转速—温升实测，也没有统一的触觉误差/带载寿命实验。未确认的电机型号、减速比、FOC 频率、价格和用户故障率明确留空。文中取 25 mm 的接触力臂、20:1 减速比和 0.15 m 的腕部力臂，均只是教学假设，不是任何产品的测量值。

## 归档边界

原研究逻辑位置：`src/wuji-research/four-hand-comparison`。本轮只迁入阶段报告、自绘图表、小型参数表和来源记录；原 CAD、教学模型、SDK、源码、下载和运行环境继续留在原工程。

[provenance.json](provenance.json) 记录源文件、原文哈希、归档版本及外部素材身份。原报告与素材未被本轮修改。
