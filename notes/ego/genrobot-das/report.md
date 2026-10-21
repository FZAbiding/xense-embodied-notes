> 历史文档快照：原记录日期 2026-09-18，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](sources.md)。

# 简智 GenRobot DAS 具身数据采集设备调研报告

> 调研对象：DAS Ego、DAS Dex、DAS Fingers、DAS Gripper、DAS Controller\
> 调研日期：2026-09-18\
> 用途：技术选型、算法可用性评估、数采工厂规划和商务采购决策\
> 结论性质：公开资料桌面调研，不代替实机验收

## 一、执行摘要

### 1. 一句话结论

GenRobot DAS 的竞争力不在某一个传感器，而在“Ego + 手部/夹爪 + 同构机器人端 + MCAP/Matrix 数据链路”的整套产品思路。它对需要在中国本地大规模采集多模态人类演示数据的团队有吸引力；但目前公开证据不足以证明“毫米/亚毫米”定位、“长时间无感”和“数据可直接训练”这些关键商业主张。

**建议：可进入付费 PoC，不建议仅凭宣传参数直接大批量采购。** 先用与量产同版本的 2–4 套设备连续运行 2–4 周，同时验证三件事：外部真值下的轨迹精度、从原始 MCAP 到目标模型的端到端可用性、多工位环境中的单人时有效数据产出。

### 2. 对用户四类问题的直接回答

| 问题 | 简短回答 | 信心度 |
|---|---|---|
| 普通用户反馈如何？ | 公开的独立长期用户反馈极少。现有证据多为厂商内容、经销商转述、开箱/展示和少量 GitHub 问题，无法得出“口碑普遍很好”。公开问题反而暴露了 H5 转换慢、缺失 VIO 辅助文件、相机轨迹与夹爪尖轨迹语义不清等摩擦。 | 高 |
| 官方定位精度可信吗？ | 参数有吸引力，但未找到对外公开的测试轨迹、真值系统、ATE/RPE、距离/时长、场景分层和失败率。所以“毫米/亚毫米”应视为待验证的厂商主张，不应直接写入数据 SLA。 | 高 |
| Ego/UMI 原始数据可直接训练吗？ | **Ego-only** 可较直接用于视觉/视频/世界模型预训练，但不是机器人控制策略所需的动作标签。**UMI/Fingers/Gripper** 在完成 QC、合并、VIO、同步、坐标变换、action 定义、重定向和质量筛选后，才能进入策略训练。 | 高 |
| 多工位会互相干扰吗？ | 会，但可工程化控制。SUB-1G 成组设备必须使用不同频段和 sync word；Wi-Fi 上传需容量规划；VIO 会受动态遮挡、低纹理、反光、照明、振动和电磁环境影响。被动 RGB 相机本身通常不会“串台”，但场景和无线管理会。 | 中高 |
| 存储导出和长时间佩戴如何？ | MCAP 开放、可解析，是优点；但现阶段仍有 SD 卡、USB、多文件配对和 Docker/VIO 后处理的运维成本。“长时间舒适”没有独立人因数据支持；350g 头戴、双手合计约 570g Fingers、单手 490–520g Gripper 均应做班次级实测。 | 中高 |
| 商务上有竞争力吗？ | **有条件的有竞争力**：产品组合、多模态、本地化和数据服务是优势；但价格不透明、规格版本漂移、精度缺少独立基准、训练链路仍需开发，使其更适合“小批 PoC 后放量”而不是“先买百台再说”。 | 中高 |

---

## 二、调研方法与证据等级

本报告使用了以下证据，并按可信度区分：

1. **A 级：可复现的技术证据**
   - 官方公开手册、SDK、MCAP topic/schema、开源转换器和代码。
   - 本地 `xense-dataset-convert` 仓库中的 DAS-UMI 严格预检、时间对齐与 LeRobot 转换实现。
2. **B 级：真实但样本有限的用户信号**
   - GitHub issue、个人实机记录、第三方开箱。
3. **C 级：官方或商业宣传**
   - 官网性能文案、订单量、效率提升、客户数和精度宣称。
4. **D 级：本报告的工程推断**
   - 根据传感器、VIO、无线通信、UMI 训练方法和数据工厂经验做出，不冒充实测结果。

截至调研日，未找到可公开复现的第三方光学动捕对比、长时间人因研究、大样本购买者评分，也未找到针对各产品精确 SKU 的公开价目表。

---

## 三、产品定位与关键规格

### 3.1 它们不是同一类产品

| 产品 | 实际角色 | 适合的数据 | 不应被误解为 |
|---|---|---|---|
| DAS Ego | 头戴第一视角多目视觉 + IMU + 音频 + VIO 轨迹 | 场景、任务语义、全局视角、头/手上下文 | 完整的机器人 action 采集器 |
| DAS Fingers | 双指仿生手持/穿戴采集器，与 Ego 成组 | 腕部图像、IMU、开合、触觉、手部轨迹 | 五指灵巧手动作的完整替代 |
| DAS Gripper | 集成式双指 UMI 夹爪 | 腕视角、夹爪开合、触觉、IMU、VIO、音频 | 无需后处理即可部署的机器人策略 |
| DAS Dex | 23 DoF 人手全手数据手套 | 关节角、指尖轨迹、3D 触觉、腕部图像 | 已经被公开客观基准验证的成熟标准产品 |
| DAS Controller | 安装在机械臂末端的同构执行/感知夹爪 | 部署时与 Gripper 采集端对齐的视觉、触觉、开合反馈 | 人手里的遥操“手柄”，或独立的数据源 |

DAS Controller 手册明确定义为 DAS Gripper 的“同构控制器”，需通用法兰安装在机械臂上，使用 24V 供电、Type-C 通信；SDK 提供 ROS/USB 接口。它的价值是降低采集夹爪与部署末端的视角、夹爪开合和触觉域偏移，不是消除机械臂运动学与控制延迟。见 [DAS Controller 手册](https://docs.genrobot.ai/products/das-controller) 和 [Controller SDK](https://github.com/genrobot-ai/gen_controller_sdk_release)。

### 3.2 公开规格汇总

| 产品 | 主要官方规格 | 需特别注意的版本差异 |
|---|---|---|
| Ego | 6 路约 2MP 全局快门 RGB，1600×1300@30Hz，水平约 270°/垂直约 150°，6 轴 2×2 IMU 阵列，128GB SD，Wi-Fi/蓝牙/Type-C | 产品页称 350g、24h 可持续换电；手册称主机 269g + 每块电池 100g，单电池约 1h40m。“24h”不是单次充电续航。 |
| Fingers | 单设备约 1 路 2MP RGB@30Hz，150° 水平 FOV，2×2 6 轴 IMU，触觉、磁编码和 Type-C | 产品页称 300g、3.5h、42GB；2026-08 手册称 285g、典型续航 1h50m。双手约 570g，还需搭配 Ego。 |
| Gripper | 3 相机 1600×1300@30Hz，6 轴 IMU@200Hz，夹爪距离 50Hz，触觉，64GB SD，续航约 3h | 新产品页称 490g、2.5kg 夹持力、100Hz；v0.4 手册称 520g、2kg、轨迹 30Hz、触觉 20Hz。官网顶部曾出现“亚毫米”文案，但规格表是“亚厘米/<1cm”。 |
| Dex | 23 DoF，210g，手掌尺寸 150–200mm、掌宽 70–95mm，存储 64GB，续航 3h，200Hz，指尖 1mm，关节角 0.02°，触觉 0.05N/1mm | 仅找到产品页和媒体稿，未找到与 Ego/Finger 同等级的公开手册、数据 schema、SDK 和训练样例；技术承诺最强，当前公开可验证性最弱。 |
| Controller | 610g，3 种快换夹爪，3 相机@30fps，448 触点/1mm，传感/编码器 50Hz，通用法兰 | 官网的“亚毫米精度控制”是控制主张，不等于末端在任意机械臂上的绝对空间定位精度。 |

主要规格来源：[DAS Ego 产品页](https://cn.genrobot.com/products/ego)、[Ego v2.0 手册](https://docs.genrobot.ai/products/das-ego)、[DAS Fingers 产品页](https://cn.genrobot.com/products/finger)、[Finger v2.0 手册](https://docs.genrobot.ai/products/das-finger)、[DAS Gripper 产品页](https://www.genrobot.com/products/das)、[Gripper v0.4 手册](https://docs.genrobot.ai/products/das-gripper)、[DAS Dex 产品页](https://cn.genrobot.com/products/dex)、[DAS Controller 产品页](https://cn.genrobot.com/products/controller)。

**规格差异不一定意味参数虚假**，也可能是 V2/V3/V4 、预量产与量产、或不同电池/夹爪配置。但对采购方而言，这意味着报价单、数据协议和验收合同必须绑定硬件 revision、固件版本、算法镜像版本和具体指标。

---

## 四、真实用户反馈、易用性与定位精度

### 4.1 “普通用户口碑”目前不足以统计

可找到的非官方信号有：

- 一位实操者记录了 Ego + UMI 的佩戴、配对和桌面双手操作，但他明确表示多模态时间对齐、动作切片和失败回放仍在搭建，也没有宣称已获得 VLA 成功率或长期稳定性。这是很诚实、但样本为 1 的反馈。见 [DAS Ego × UMI 实机记录](https://lijinghai.github.io/RabbitRobot/projects/rabbitrobot-ego-umi.html)。
- 美国一机器人中心的开箱视频展示了 Finger 启用前的零点校准和 Ego/Finger 连接，证明基本流程可操作，但不是精度、耐久性或舒适度评测。见 [Robotics Center of Silicon Valley 开箱](https://www.linkedin.com/posts/roboticscenter_robotics-genrobot-roboticshardware-activity-7501405912264298498-0c1p)。
- Genrobot iOS App 在调研时还没有足够评分/评论形成概览，版本历史仍在重构同步录制组网、连接和自动上传。见 [Apple App Store 页面](https://apps.apple.com/us/app/genrobot/id6758616332)。
- 电商搜索页可见 Ego 仅少量评论计数，Gripper/Fingers 更少，且无法确认是否为实际交付后的技术用户，不足以作为口碑样本。

因此，对“实际普通用户反馈如何”最负责的答案是：**无法从公开资料判定；公开用户基数和使用时间都太少。** 任何“已广泛好评”或“实际很难用”的强结论都超出现有证据。

### 4.2 目前最有价值的负面/摩擦信号来自开源工具用户

GenRobot 官方 `das-datakit` 在调研时只有少量 issue，但内容非常具体：

- [Issue #1](https://github.com/genrobot-ai/das-datakit/issues/1)：用户报告 MCAP 转 H5 很慢。
- [Issue #2](https://github.com/genrobot-ai/das-datakit/issues/2)：用户能解析开放数据，但不知道怎样在机械臂和策略模型上评估。
- [Issue #6](https://github.com/genrobot-ai/das-datakit/issues/6)：开放数据中找不到 `vio_info.json` 或 `success_mcap`，用户不确定如何生成。
- [Issue #14](https://github.com/genrobot-ai/das-datakit/issues/14)：用户质疑所谓 EEF 轨迹实际上是相机轨迹，询问相机到夹爪尖的外参变换。

这些 issue 不能证明硬件不好，却直接证明了一点：**“文件可打开”与“动作语义清楚、可复现训练”之间还有不小的工程距离。**

### 4.3 易用性：采集操作简单，数据生产系统不算简单

**优点**

- Ego 可通过 App 扫码连接，查看电量、SD 卡、头姿和遮挡，一键开始/结束。
- Ego + Finger 可快速配对，三次快速闭合夹爪可触发录制。
- Gripper 本体有屏幕、容量/电量/触觉/开合实时显示，按键即录制，不需要连接机械臂。
- 原始容器为 MCAP，proto 和解析工具公开，不是完全封闭的二进制黑箱。见 [das-datakit](https://github.com/genrobot-ai/das-datakit)。

**摩擦点**

- Ego + 双 Finger 原始数据是 3 个 MCAP，需依赖一致 `group_uuid` 配对；缺任一角色的数据组会被跳过。
- 官方后处理不是一步导出，而是 `qc → merge → vio → vio_check`，推荐 Linux x86_64、16 核 CPU、32GB RAM、Docker 和足够磁盘。见 [Finger 手册的处理流程](https://docs.genrobot.ai/products/das-finger)。
- Matrix Studio 要求 Linux、Docker 和 GPU，Web 端登录凭证随订单获取；算法镜像与设备版本绑定。见 [Matrix Studio 手册](https://docs.genrobot.ai/products/matrix-studio)。
- 手册与产品页对上传功能的表述不一致：产品页称无缝云端上传，Finger 手册则提示当前用户应从 SD/设备拷贝，Gripper v0.4 手册把 Wi-Fi 上传标为“Coming soon”。这可能是固件代际差异，必须按交付版本实测。

所以，对单个采集员来说“开始录制”很容易；对数据工程团队来说，想要稳定产出可训练数据，仍需要版本管理、计算集群、预检、失败重试、数据盘点和标注流程。

### 4.4 “毫米级”定位应怎样理解

| 产品 | 官方文案 | 本次能核实的内容 | 评价 |
|---|---|---|---|
| Ego | 毫米级轨迹重建 | 确认存在 6 目 + IMU + VIO 输出和 VIO checker；未见外部真值基准 | 技术路径合理，精度数值未独立证实 |
| Fingers | 毫米级轨迹 | 确认有 RGB/IMU/磁编码、Ego 共世界坐标的 VIO topic | 对纹理、光照、运动和 Ego 配对有条件依赖 |
| Gripper | 新规格表称亚厘米，部分页头文案称亚毫米 | 手册明确写 `<1cm`；开合旋转轴精度 ±0.2° 是另一指标 | 应以合同中的可验收数值为准，不引用页头口号 |
| Dex | 亚毫米轨迹、1mm 指尖、0.02° 关节 | 未见公开手册、标定规程、精度分布或实测数据 | 高潜力、高验证风险 |
| Controller | 亚毫米精度控制 | 有编码器/目标开合距离 ROS topic | 夹爪开合分辨率不等于机械臂 TCP 绝对定位精度 |

VIO 轨迹“短时局部很平滑”、“起终点距离很小”与“全轨迹对真值是毫米级”不是一回事。官方 checker 检查轨迹长度、掉帧、坐标范围和 jerk，能发现坏轨迹，但没有外部 ground truth 就不能证明绝对精度。

**签约前应要求厂商提供：**

1. 相同硬件/固件版本在 Vicon/OptiTrack/激光跟踪仪下的原始轨迹和评测脚本。
2. ATE RMSE、RPE（平移/旋转）、终点漂移、尺度偏差、轨迹中断率，不只是单个“精度”数字。
3. 分场景结果：低纹理、反光金属、渐暗、快速运动、动态人员遮挡、5/30/60 分钟轨迹。
4. 相机光心、设备 `base_link`、夹爪尖/TCP 之间的标定矩阵、温漂和重标定频率。
5. 所谓 `<1ms` 同步的时钟定义、测量位置、P50/P95/P99/max，以及断联后的时钟行为。

---

## 五、数据能否直接作为模型训练数据

### 5.1 结论先行：要看训什么模型

| 目标模型 | Ego-only | Ego + Fingers / Gripper / Dex | 是否可直接用原始数据 |
|---|---|---|---|
| 视觉/视频表征、行为理解、世界模型预训练 | 很有价值 | 可增加腕视角和接触信号 | 视频解码、切片、标注和隐私处理后可用，但不是零处理 |
| VLM/VLA 的语义预训练 | 可用作视觉上下文 | 动作/触觉可作额外监督 | 需要任务文本、时间段、成功/失败和数据配方 |
| 双指夹爪 Diffusion Policy / ACT | 缺少可部署 action | Gripper/Fingers 更适合 | **不可直接**；需要 VIO、TCP 外参、相对动作、延时对齐、机器人约束和训练格式 |
| 五指灵巧手策略 | 可提供全局视野 | Dex 潜在价值最高 | **不可直接**；需人手到机器手重定向、自碰/关节/力限制、触觉标定和机器人真机微调 |
| 头戴手势/人体重建 | Ego 可以输出 21 手部关键点 | Fingers/Dex 可增加真值或近似真值 | 需坐标系核对、可见性筛选和关键点质量估计 |

### 5.2 为什么 Ego 视频不能直接变成机器人 action

Ego 官方数据可包含 6 路 RGB、200Hz IMU、头部 6D VIO、音频、左右手 21 个 3D 关键点和帧有效性标记。具体 topic 见 [DAS Ego Data Introduction](https://docs.genrobot.ai/guides/das-ego-data-introduction)。

但机器人策略通常需要的 action 是下一时刻/一段 horizon 的 TCP 位姿、夹爪开合、关节命令、力/阻抗命令或它们的增量。头部轨迹和人手关键点不等于这些命令，也不自带机器人的可达性、碰撞和执行器动力学。

因此 Ego-only 更适合：

- 视觉表征和场景理解预训练；
- 任务分段、动作识别、手物交互理解；
- 世界模型、视频预测、头戴视角 VLM；
- 与同步 UMI/机器人数据做跨视角对齐。

如果要训控制策略，Ego 应是全局观测通道，而不是唯一的 action 来源。

### 5.3 UMI 数据也不是“拿到就训”

原始 UMI 研究的可部署性不只来自“有一个夹爪”，而来自精心设计的相对轨迹 action、视觉/夹爪/机器人延迟匹配、双手相对位姿、运动学可行性和机器人部署接口。见 RSS 2024 [Universal Manipulation Interface](https://real.stanford.edu/umi/) 及其 [训练配置](https://github.com/real-stanford/universal_manipulation_interface/blob/main/diffusion_policy/config/task/umi.yaml)。

对 DAS 数据，建议的生产链路是：

```text
原始 MCAP
  ↓ 完整性与传感器 QC
同一 group_uuid 的 Ego / Left / Right 合并
  ↓ VIO / SLAM + VIO checker
带轨迹的 merged MCAP
  ↓ 统一时钟、去坏帧、多频率重采样
观测时间线（RGB / IMU / tactile / encoder / pose）
  ↓ 相机光心→夹爪 TCP，world/local/relative 坐标统一
EEF pose + gripper state + contact
  ↓ 定义 relative/delta/chunked action，匹配推理延时
模型所需 action
  ↓ 机器人可达性/碰撞/速度过滤，任务切片与成败标注
LeRobot / RLDS / Zarr / 项目自定义格式
  ↓ 基线训练 + 离线回放 + 真机安全验证
可部署数据集
```

### 5.4 拿到原始数据后的必做后处理

#### A. 文件和 schema 层

1. 校验 MCAP 可读、文件大小、hash、录制时间、设备 ID、firmware 和 `group_uuid`。
2. 盘点 topic/schema/频率，防止固件升级后 topic 或单位漂移。
3. 保留原始文件为不可变更层，转换产物另存，不覆盖原始数据。

#### B. 质量和时间层

1. 解码每一路视频，检查中途损坏、分辨率变化、掉帧和 sequence gap。
2. 检查 `header.timestamp` / `log_time` / `publish_time` 是否一致，不应逐消息混用时钟。
3. 以目标频率建立整数纳秒时间网格，保留每个输出样本的原始 timestamp 和 source index。
4. 计算近邻配对 gap、重复样本、未选样本和多相机时间跨度。
5. 使用官方 `frame_validity` / `time_range_validity` 但不盲信，对解码、轨迹和帧内容再做独立 QC。

#### C. 几何和 action 层

1. 明确 `eef_pose` 究竟是相机、`base_link` 还是真正夹爪 TCP；应用 URDF/手眼标定转换到模型约定的坐标。
2. 将 quaternion 统一顺序、归一化并转为模型所需的 axis-angle/6D rotation，避免四元数符号跳变。
3. 将磁编码器原始值标定为米、弧度或归一化开口宽度，不能靠字段名猜测。
4. 根据策略定义 action：下一帧绝对 pose、当前 TCP 坐标下的相对 pose、delta pose，或多步 action chunk。
5. 双手需保留两夹爪相对位姿；Dex 需从人手 23 DoF 重定向到目标机器手的自由度。
6. 按目标机器人检查 IK、工作空间、关节限位、速度/加速度、自碰与环境碰撞。

#### D. 训练数据层

1. 按语义任务切 episode，去掉开始/结束手势、静止初始化和无意义尾段。
2. 标记任务指令、对象、场景、操作者、成功/失败、失败类型和接触阶段。
3. 训/验/测应按场景、操作员或物体切分，不能随机分帧造成泄漏。
4. 计算标准化统计，对 RGB 的鱼眼畸变/裁剪/缩放配方做版本化。
5. 先运行一个小数据基线，能过拟合 10–50 条 episode，再扩展数据工厂。

### 5.5 本地 `xense-dataset-convert` 已解决什么，还没解决什么

本项目已经实现一条比官方简单 `mcap_to_h5` 更严格的 DAS-UMI 到 LeRobot v3.0 管线，详见 [`xense-dataset-convert/docs/mcap2lerobot.md`（工作区资料，未随文保存）](sources.md#workspace-0a5b1930fc2a) 和 [`configs/das_umi.yaml`（工作区资料，未随文保存）](sources.md#workspace-31a7fe342f16)。

已有能力包括：

- 完整解码八路视频做预检，检查必需流、非有限数、时间倒退/重复、序列丢失、中途视频损坏、分辨率变化和同步超差。
- 使用 30Hz 整数纳秒网格，对齐 8 路视频、3 路 IMU、2 路磁编码和 pose，保留每路 source timestamp/index。
- 保留标定 topic 为 JSON 元数据，输出预检和转换报告。
- 输出前检查 Parquet 行数、时间线、视频帧数/分辨率和 action 一致性，通过后再原子发布。

仍需注意：

- 默认合并采集的 `observation.state` 是两个编码器原始值 + 9D 头部 pose，共 11 维；左右手 pose topic 为可选配置，不配时不会自动出现。
- `--export-action` 的语义是 `action[t] = observation.state[t+1]`，这是数据表达上的一步平移，**不等于已经得到目标机器人的可执行命令**。
- pose 目前是 XYZ + rotation-6D，没有自动做相机到夹爪 TCP 坐标变换。
- 配置中对编码器的物理单位未验证，因此保留为 `raw_value`。
- 音频、深度、系统状态等未配置 topic 只盘点不转换，需按项目增补。

换言之，这条管线已能把“不可靠的原始时序”变成“可审计的 LeRobot 观测数据”，但具体模型的 action 定义、TCP 外参和机器人重定向仍是算法团队的责任。

---

## 六、多工位数据工厂评估

### 6.1 多工位互相干扰

#### 1. RF 配对干扰：明确存在，也有明确规避方法

DAS Gripper V4 双手同步使用 SUB-1G。官方手册明确要求：同组使用相同频段和 sync word，不同组在同一区域使用不同频段和 sync word，否则可能互相干扰。见 [双手采集 V2.0 指南](https://docs.genrobot.ai/guides/dual-das-gripper-v2)。

工厂应把设备组识别码、频段、sync word、工位和操作员写入中央配置表，不允许采集员随意选择。每次上电后重新确认 RF 配置和信号强度。

#### 2. Wi-Fi 拥塞：更影响配置/预览/上传，本地录制风险较低

设备有本地 SD/内部存储，所以设计上不应把实时 Wi-Fi 作为原始数据唯一通道。但多工位同时 RTSP 预览、OTA、日志和上传会抢占带宽和 AP airtime。建议：

- 采集 VLAN 与办公网分离，按 AP 和频段做容量规划；
- 录制期禁止批量 OTA 和云上传；
- 数据上传放在休息/换班窗口，或使用有线读卡集中导入；
- 验收时同时开启目标规模数量的工位，不只测单机。

#### 3. 视觉/VIO 环境不会“网络串台”，但会被环境集体影响

被动 RGB 相机之间通常没有类似多台结构光深度相机的主动光串扰问题。但多人同场会增加动态遮挡，相同空桌、反光零件、频闪照明和近距离交叉会降低 VIO 稳定性。

官方 Ego/Finger 手册的环境要求实际上相当严格：照度 `≤500 lux`、无直射光/强反光、地面无振动，并远离电机、变频器、大功率电源和 Wi-Fi 6E/5G 基站，磁场 `≤50mT`。这与常见的亮照工业工位、金属反光件和电机生产线有明显冲突，应作为 PoC 核心项，不能当作手册小字忽略。

### 6.2 数据存储和导出

**积极面：**

- 原始格式 MCAP 适合多传感器时序，有公开规范、proto 和 Python 工具。
- Ego 原始数据可从 SD 卡拷贝；Finger 可从 Type-C 拷贝；Gripper 可读 SD 卡。
- Ego App 已支持无 Matrix 模式，可填入对象存储凭证做自动/手动上传，前提是所交付固件确实支持。
- Matrix/Monitor 能盘点 topic、帧率、时长和轨迹，适合运营人员快速回看。

**运营负担：**

- Ego + 双 Finger 每条 episode 是 3 份原始文件，合并后还有中间产物、debug 目录和转换数据集。
- 官网的“压缩到原始体积 2%”没有说明“原始”是未压缩 RGB，还是现有 H.264 MCAP，也没有码率/画质条件，不能直接用于存储预算。
- 视频码率、平均 episode 时长和失败重录率未公开，无法从规格表可靠地算出 GB/人时。

**建议的工厂存储架构：**

```text
工位本地录制（SD / 内置存储）
  ↓ 换班导入站（设备 ID + UUID + hash + 快速完整性检查）
对象存储 Raw 不可变更区
  ↓ 异步 qc / merge / vio / vio_check
Processed MCAP + 质量报告
  ↓ 数据版本化转换
LeRobot / Zarr / RLDS 训练区
  ↓
元数据目录（任务、人、场景、设备/固件、质量、权利和血缘）
```

不建议边录制边把云上传当作唯一持久化方式。工位先落本地、结束后做 hash 和快速 QC，能将无线异常与原始录制风险分离。

### 6.3 采集员长时间舒适度

没有找到独立的 4/8 小时人因测试，因此以下是基于重量和形态的工程风险判断，不是实测结论：

- **Ego：**约 350–369g 集中在头部。官方手册要求紧贴眉部、保持水平且头发不遮挡镜头。变动工位中可能有额头压迫、闷热、头围适配和快速转头惯性问题。在头戴对比市场中，Meta Aria Gen 2 约 75g、部分国产 Ego 约 157–235g；DAS 的 6 目大 FOV 是优势，但重量不是同类最低。比较见 [Ego 设备公开汇总](https://github.com/EmbodiedAI-Group/awsome-ego-equipments)。
- **Fingers：**手册约 285g/只，双手约 570g，另有 Ego 头戴重量。它的优势是仿生两指和较大开口；风险是手腕负荷、长时间重复握合和小尺寸物体的手指可达性。
- **Gripper：**单只 490–520g，双手合计约 1kg，还需反复扣动机构。“可连续 3 小时无疲劳”是厂商主张，未见用户研究。可以参考竞品 TRumi 把 0.4lb 触发力和恒力弹簧作为长时使用的明确人因指标，而 DAS 公开资料没有给出触发力曲线。
- **Dex：**210g 比双指夹爪更轻，但全手 23 DoF 机构可能带来关节限制、手型匹配、触觉位点压迫和清洁消毒问题；现有公开资料不足以判断。
- **Controller：**正常情况安装在机械臂上，不应纳入人体长时间穿戴负担。

建议工位安排为 45–60 分钟采集 + 5–10 分钟休息/换电/数据导入，在 PoC 中收集颈部、手腕、手指、视觉疲劳和热感的 0–10 主观量表，再决定班次强度。

---

## 七、市场与商务竞争力

### 7.1 实际对手不只是另一家 UMI

| 路线 | 代表 | 相对 DAS 的优势 | 相对 DAS 的弱点 |
|---|---|---|---|
| 开源/DIY UMI | Stanford UMI | 论文、硬件、训练与部署代码全链路公开，社区可复现 | 装配、标定、耐久性和维护门槛高，触觉/整机产品化弱 |
| 产品化 UMI | TRumi、Pika、觅蜂、FastUMI 等 | 部分价格透明、生态与 Diffusion Policy 紧密，或有商用 tracker 降低 VIO 复杂度 | 不一定同时具有 DAS 的 Ego + 触觉 + 双手 + 机器人端组合 |
| 头戴 Ego | Meta Aria Gen 2、KAI Halo、FastUMI Ego、Primus Ego 等 | 一些设备显著更轻，或有 HDR/眼动/深度，部分有公开价 | 往往没有 DAS 的 6 目超宽视野与 Finger/Gripper 成组链路 |
| 机器人本体遥操 | 主从臂、VR/动捕、同构臂 | action 原生符合目标机器人，几何/动力学域差小，成功率最容易闭环 | 设备成本、工位空间、操作速度和扩展成本高 |
| 商业数据服务 | 采集工厂/数据供应商 | 客户不需自建运营和标注体系 | 数据权属、定制速度、可审计性和长期成本受供应商约束 |

TRumi 已公开双机套价：不含 GoPro 约 949.95 美元，含两台 GoPro 约 2,195.99 美元，支持 MCAP/Zarr，但不是触觉和 Ego 全套的等价比较。见 [TRumi 产品页](https://www.trossenrobotics.com/trumi)。FastUMI 则用商业 tracker 替换复杂 VIO，并强调自动 QC 与模仿学习集成，见 [CoRL 2025 论文](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html)。

### 7.2 DAS 的核心商务优势

1. **产品组合完整**：头戴 Ego、双指 UMI、全手 Dex、夹爪采集器、机器人端 Controller 和 Matrix 构成完整叙事，适合客户从视觉预训练过渡到操作策略。
2. **多模态和超宽视野**：DAS Ego 6 路全局快门和 Fingers/Gripper 的触觉、IMU、编码器组合，比单 GoPro UMI 的信号更丰富。
3. **本地采集和国内支持**：对中国企业，本地售后、国内镜像、中文运营和批量交付比海外开源系统更可控。
4. **数据与服务一体化**：不只卖硬件，还可卖原始/处理/模型级数据，对不想自建数据工厂的客户具有商务吸引力。
5. **MCAP 和部分开源生态**：至少原始格式、proto、解析 SDK、Controller SDK 和部分数据是可访问的，锁定程度低于完全封闭方案。

公司声称 Ego/Fingers/Gripper 累计订单过万，但这是厂商宣传稿转载，应与已交付、验收、复购和活跃设备数区分。原文转载页自身也声明不对信息真实性作保证，见 [界面新闻转载](https://www.jiemian.com/article/14277466.html)。

### 7.3 主要商务弱点与风险

1. **公开价格不透明**：无法与已公开价格的 TRumi/KAI Halo 做真正 TCO 比较。报价必须拆分硬件、备件、平台授权、算法镜像、云存储、支持和数据服务。
2. **参数和功能随版本漂移**：重量、续航、夹持力、触觉频率、精度口径和云上传状态在不同页面不一致。
3. **精度没有公开独立基准**：这是影响高价采购最大的技术信任缺口。
4. **“Model-ready”仍有语义缺口**：夹爪尖外参、action 定义、目标机器人可达性和推理延迟不会因转成 H5/LeRobot 而自动消失。
5. **部分管线依赖厂商镜像/凭证**：需在合同中明确离线镜像使用权、版本锁定、停服后可用性和私有化部署。
6. **公开开发者生态尚年轻**：`das-datakit` 有一定 star/fork，但 issue 样本小、部分问题尚无公开回复，还不是成熟标准生态。
7. **Dex 成熟度证据不足**：公开的产品参数很亮眼，但文档、schema、开发套件和第三方实测没有跟上 Ego/Finger/Gripper。

### 7.4 综合判断

| 维度 | 评价 | 说明 |
|---|---|---|
| 产品理念 | 强 | 头+手+触觉+机器人端的组合有差异化 |
| 传感器配置 | 中强 | 6 目 Ego、多模态 UMI 和 Dex 信号丰富 |
| 采集端易用性 | 中强 | 按键/App/屏幕友好，但配对、版本和导出有操作成本 |
| 算法端易用性 | 中 | 格式公开，但 QC/VIO/坐标/action/重定向仍需开发 |
| 公开性能证据 | 弱 | 缺独立定位基准、人因实测和长期可靠性数据 |
| 数采工厂适配 | 中 | 有工厂模式和组网设计，但环境约束、RF/Wi-Fi 和手工导出需规划 |
| 生态/锁定风险 | 中 | MCAP/SDK 降低锁定，VIO/Matrix 镜像和凭证增加依赖 |
| 商务性价比 | 暂无法判定 | 没有公开可比报价，且需计入后处理与运营 TCO |

---

## 八、建议的 PoC 与采购验收方案

### 8.1 不要只测“能不能录制”

建议采购与算法团队共同定义以下闸门：

#### 闸门 A：硬件和人因

- 2–4 工位同时运行，每天两个 2 小时采集块，连续至少 10 个工作日。
- 统计开机/配对/校准耗时、电池更换、异常重启、连接丢失、SD/USB 拷贝故障和设备日利用率。
- 每 30/60 分钟记录头颈、肩、腕、手指疲劳和压痛，记录体型/头围/手型差异。

#### 闸门 B：传感器与同步

- 每路实测频率、P99 间隔、掉帧率、中途解码错误、分辨率漂移。
- 不仅验证平均同步，还验证 P95/P99/max 和长时时钟漂移。
- 在目标工厂的灯光、反光零件、电机/变频器、Wi-Fi 和人员密度下实测，不在厂商实验室代替。

#### 闸门 C：定位与几何

- 用外部真值比较 1/5/15/60 分钟轨迹，包含静态、慢速、快速、回环、遮挡、低纹理和反光场景。
- 分别计算相机光心、设备基座和夹爪 TCP 轨迹误差。
- 验证每台设备、多次上电、多个温度和多个操作员，报告均值、P95 和失败率。

#### 闸门 D：数据管线

- 从设备上一条原始 episode 开始，无人值守地完成 ingest、QC、merge、VIO、转 LeRobot/Zarr 和数据盘点。
- 人为制造缺文件、重复 UUID、坏包、掉帧、时钟跳变、磁盘满和网络中断，验证可追溯失败和重试。
- 测量 GB/原始人时、GB/有效人时、后处理算力分钟/数据分钟、转换增幅、保留周期和备份成本。

#### 闸门 E：模型闭环

- 选 2–3 个代表任务：简单 pick-place、高精度插入/开合、一个双手任务。
- 按最终部署的 action 语义训一个基线模型，与机器人原生遥操数据做同数量对照。
- 记录成功率、接触失败、碰撞、超界、动作抖动和推理延时；没有真机闭环成功，就不应把数据定义为 model-ready。

### 8.2 建议写进合同的条款

1. **SKU 和版本**：硬件 revision、传感器型号、镜头、固件、App、Matrix、VIO 镜像和 SDK 版本。
2. **数据字典**：topic/schema、单位、坐标系、四元数顺序、时钟来源、标定文件和版本兼容承诺。
3. **可验收性能**：不写“毫米级”，写明指定轨迹/场景的 ATE/RPE/P95/失败率；不写“<1ms”，写明时钟和分位数。
4. **离线可用性**：镜像离线包、license 期限、无云网络使用、停服/公司变更后的数据可读性。
5. **数据权利与安全**：原始数据、衍生数据、标定参数和日志的权属；云上传地域、删除和审计；加密 MCAP 的永久解密能力。
6. **支持与维修**：固件回退、RMA SLA、备机/备电池/夹爪头/线材库存、批量故障通报。
7. **接口稳定性**：发布前通知周期、schema 迁移工具、老数据的长期兼容。
8. **真实 TCO**：硬件单价外，列明平台授权、算法、云、数据处理、培训、标注、维保和版本升级费用。

---

## 九、分场景采购建议

### 场景 A：主要做大规模 Ego 视频/世界模型预训练

**建议：值得 PoC，优先级较高。** 6 目超宽视野、全局快门、IMU、音频、手部关键点和本地 MCAP 是实际优势。采购重点应是舒适度、画质/HDR、遮挡、数据量、隐私流程和数采成本，而不是过度执着于毫米级头部轨迹。

### 场景 B：主要训双指夹爪策略

**建议：Gripper + Controller 是最有商业逻辑的组合，但必须做机器人闭环 PoC。** 同构末端能减少视角、夹爪开合和触觉域差；但需验证 TCP 外参、机械臂控制频率、延时匹配和实机成功率。

### 场景 C：要做高自由度灵巧手

**建议：Dex 仅做技术评估/早期试用，暂不作为唯一量产数据源。** 采购前必须获得真实训练数据样例、schema、标定流程、手型适配范围、触觉标定、目标机器手重定向工具和至少一个第三方机器人成功案例。

### 场景 D：建多工位数采工厂

**建议：先买小批量、同时投入数据平台和运营工程。** 不要只做硬件 BOM，应把导入站、对象存储、算力队列、QC 报表、设备/固件管理、标注系统、人因排班和备件库一并纳入预算。多工位的经济性取决于“每个付费人时产出多少分钟通过 QC 且最终能训练的数据”，而不是录制按钮按了多少次。

---

## 十、最终决策意见

1. **DAS Ego：建议进入 PoC。** 在超宽多目 Ego 采集上有明显产品特色，但要重点测头戴舒适度、工厂光照与 VIO 失败率。
2. **DAS Fingers：适合 Ego 的双手补充，不应单独按“可直训机器人”采购。** 需验证轨迹、开合单位、触觉、长时手腕负担和 Ego 组网稳定性。
3. **DAS Gripper + Controller：是最容易形成“采集—训练—部署”商业闭环的产品对。** 但前提是用真机基线证明同构确实带来成功率收益。
4. **DAS Dex：暂定“高潜力、低证据成熟度”。** 没有手册、数据契约和独立实测前，不应按亚毫米精度和 1ms 延迟做量产投资回报测算。
5. **整体品牌：有竞争力，但采购策略应是“用可量化验收换批量订单”。** 最大的风险不是录不到视频，而是采集了大量“可观看、可解析，但动作语义不对或不能在目标机器人上闭环”的数据。

---

## 附录 A：重点资料索引

### GenRobot 官方

- [DAS Ego 产品页](https://cn.genrobot.com/products/ego)
- [DAS Ego v2.0 手册](https://docs.genrobot.ai/products/das-ego)
- [DAS Ego 数据 topic 与坐标系](https://docs.genrobot.ai/guides/das-ego-data-introduction)
- [DAS Fingers 产品页](https://cn.genrobot.com/products/finger)
- [DAS Finger v2.0 手册](https://docs.genrobot.ai/products/das-finger)
- [Ego-Finger 合并数据说明](https://docs.genrobot.ai/guides/das-ego-finger-data-introduction)
- [DAS Gripper 产品页](https://www.genrobot.com/products/das)
- [DAS Gripper v0.4 手册](https://docs.genrobot.ai/products/das-gripper)
- [DAS Gripper V4 双手无线采集指南](https://docs.genrobot.ai/guides/dual-das-gripper-v2)
- [DAS Dex 产品页](https://cn.genrobot.com/products/dex)
- [DAS Controller 产品页](https://cn.genrobot.com/products/controller)
- [Matrix Studio 手册](https://docs.genrobot.ai/products/matrix-studio)
- [das-datakit：MCAP/H5 解析与转换](https://github.com/genrobot-ai/das-datakit)
- [das-ego-stack：qc/merge/vio/vio_check](https://github.com/genrobot-ai/das-ego-stack)

### 第三方、用户与基准方法

- [DAS Ego × UMI 实机记录](https://lijinghai.github.io/RabbitRobot/projects/rabbitrobot-ego-umi.html)
- [Genrobot iOS App 及公开评分状态](https://apps.apple.com/us/app/genrobot/id6758616332)
- [das-datakit 公开 issues](https://github.com/genrobot-ai/das-datakit/issues)
- [UMI 论文/项目页](https://real.stanford.edu/umi/)
- [FastUMI, CoRL 2025](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html)
- [TRumi 产品与公开价格](https://www.trossenrobotics.com/trumi)
- [Ego 数采设备公开参数汇总](https://github.com/EmbodiedAI-Group/awsome-ego-equipments)

## 附录 B：需向 GenRobot 当面确认的 15 个问题

1. 报价对应的 Ego/Finger/Gripper/Dex 硬件 revision 和当前量产固件是什么？
2. 各 SKU 实际含电池重量、单次续航、电池寿命和换电中断时间是多少？
3. 毫米/亚毫米精度的真值设备、轨迹长度、指标定义、样本量和 P95 是什么？
4. `<1ms` 是传感器硬件触发差、设备时钟差、写入时间差，还是端到端延迟？
5. `eef_pose` 的原点是相机光心、IMU、`base_link` 还是 TCP？相互外参是否每台交付？
6. 磁编码器字段的物理单位、标定公式、温漂和重校频率是什么？
7. 触觉是原始 ADC、压力、三维力还是压力图？每个触点的标定和饱和/滞回如何？
8. 当前交付版是否真正支持客户自有 S3/OSS 直传，还是必须手工读卡？
9. MCAP 是否加密？客户能否在不联网、不依赖厂商服务的情况下永久解密？
10. Matrix/VIO 镜像是否包在硬件价格？是永久授权还是订阅？能否离线私有化？
11. 多工位可用的 SUB-1G 频段/sync word 组合数、同地域实测上限和监控工具是什么？
12. 手册中 `≤500 lux`、远离电机/变频器等要求是保守建议还是超出即不保证性能？
13. Dex 的完整手册、schema、样例数据、SDK、标定和机器手重定向工具何时可提供？
14. 能否提供一个从指定量产设备原始 MCAP 到公开模型训练、再到 Controller 真机成功率的可复现完整案例？
15. 批量部署的 DOA/RMA/备机率、一年内故障率、镜头/夹爪/触觉耗材价格和交付周期是什么？
