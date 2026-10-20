# 来源与素材

## 一手来源与版本

<a id="source-version"></a>

| 来源 | 链接或标识 | 版本/日期 | 支持的内容及边界 |
|---|---|---|---|
| 原工程文档快照 | 工作区逻辑名称 `xense-genie_sim`；主文档位于 `wbc_demo/` 与 `wbc_demo/umi_replay/` | `5015ce3d4acc61258a0184b1a008a003f67d8a22`；WBC/UMI 记录 2026-10-12 至 2026-10-19 | 原学习解释、计算、仿真与过程报告；本轮未重跑，原执行者真实身份未独立核实。 |
| 原工程引擎配套文档 | `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/` 中 7 份文档 | 同一捕获提交；各篇原研究日期未知 | [工程摘编](topics/engine-review.md)，不把设计验收方案写成测试结果。 |
| Genie Sim 公开上游 | [AgibotTech/genie_sim](https://github.com/AgibotTech/genie_sim) | 原报告引用入口；与本地 fork 的逐项版本映射未建立 | 背景入口，不代表公开上游与本地文档/代码相同。 |
| 原实验使用的场景/机器人资源入口 | [GenieSimAssets](https://huggingface.co/datasets/agibot-world/GenieSimAssets) | 原报告未为全部资产提供统一 revision | 资源身份与获取入口；没有下载或迁入整套资源。 |
| XTac UMI 数据 | [TacVerse/xtac-umi-g1-block-to-box 固定版本](https://huggingface.co/datasets/TacVerse/xtac-umi-g1-block-to-box/tree/8ad651578fda4724514387e2d3d3551c3c9631f9) | `8ad651578fda4724514387e2d3d3551c3c9631f9` | 原报告记载 11 段 / 13,500 帧 / 30 Hz；没有迁入数据集。原媒体说明记载许可 CC-BY-SA-4.0，本轮未联网重验数据卡。 |
| 原坐标审阅的本机采集代码 | 工作区逻辑名称 `TacCap-core`、`lerobot-xense` | 原报告记录提交分别为 `40255689fd44c3b66310dfb3e63d686e30ddc737`、`1de0dc8bd9c94a0046b52fe6677f87d6e7b93809` | 导出机制与 world / EEF 语义；原报告明确不能断言它们就是历史数据的导出版本。本轮未迁入、未复核这些代码。 |
| 运动学与控制背景 | [Pinocchio](https://github.com/stack-of-tasks/pinocchio)、[BioIK](https://github.com/TAMS-Group/bio_ik)、[MoveIt Servo](https://moveit.picknik.ai/main/doc/examples/realtime_servo/realtime_servo_tutorial.html)、[Pink](https://github.com/pink-kinematics/pink)、[TSID](https://github.com/stack-of-tasks/TSID) | 原报告引用入口，非本轮新调研；Pinocchio 本地实验版本记载为 4.1.0 | 职责与学习背景；不据当前网页或上游版本推定本地实验状态。 |

本地提交用来定位受限工作区的快照，不能冒充公开可访问的源码固定提交。账号、人员信息与私人远端地址不随文发布。原报告里的其他外链保留其历史身份，本轮未联网核验可用性与内容变更。

## 原研究与迁入

2026-10-19 按明确文件清单复制，保持原文件完整：23 份 WBC/UMI 主文档、11 份媒体来源说明、32 项实际使用的图片/动图/精选视频；另外从 7 份引擎文档摘编 1 篇复盘。捕获时间细分为文档与媒体，见 [provenance.json](provenance.json)。每份源文件记录相对逻辑路径、原文 SHA256、源提交、迁入位置、迁入版 SHA256 和改动方式；捕获内容逐项与该提交比对一致。

迁入保持技术结论、旧结果、撤回、失败与版本差异；增加历史快照提示，修复交叉链接，注明原工程命令的使用边界。全身 IK 入门中私人 worktree / 远端同步操作节删节，账号和私人仓库地址省略；单独的 `wbc_demo/MIGRATION.md` 不迁入，因为其内容主要是备份、目录与远端操作。必要的技术版本已在本页定位。正文只保留原有教学公式和历史调用命令，没有复制工程实现文件。

媒体只保留逐项列出的内容，图片与视频字节未改动。相同内容的 HTML 导出、原始 manifest / 执行报告 / CSV 及其余视频仍在工作区；原媒体说明保留为历史来源证据，并在每篇开头及末尾标出本次保留范围，不能将其理解为原验收包完整镜像。

入口 `source_date` 使用最早明确的 WBC 记录日期 2026-10-12；原研究持续到 2026-10-19，引擎各篇研究日期未明确。建档和迁入日期为 2026-10-19。文档以后仍可能变化，本包只涵盖此次捕获的哈希。

## 证据边界

- 原文中的测试次数、耗时、误差、成功/失败和浏览器操作均属于原报告记载，本轮没有重新执行。
- 仿真反馈关节 FK 的“实测”不等同于外部物理定位；模型数值一致性不等同于硬件精度。
- 阶段变化通过 [阅读时间线](report.md)说明：早期虚拟 EEF、夹爪只记录、离线关键帧与原速在线模式不能混用。
- 原始日志与模型未随文保存，读者仅凭本包不能重做全部实验审计。源 SHA256 定位原件身份，迁入 SHA256 用来核查当前笔记文件。
- 本轮检查文件清单、哈希、相对链接、索引、脱敏及收录边界；核对精选 PNG/GIF/SVG 可读取，使用现有解码器完整解码精选 MP4 的 1,250 帧（30 fps、41.666667 s）。媒体可读性检查不构成运动验收；没有新仿真、真机或网络来源核验。

## 素材来源与许可

逐项清单见下表，源文件路径和 SHA256 在 [provenance.json](provenance.json) 的 `assets` 中。生成方式继承各媒体目录原说明，具体作者身份未知。

含源采集画面的素材由 TacVerse 公开数据衍生，原说明记载缩放、抽帧、拼接、标题或源相位重采样；源画面及相关衍生部分保留 **CC-BY-SA-4.0** 署名与许可边界。仿真模型、独立渲染、教学图和诊断图未逐项明确单独许可时，标为未知，本仓库不代为统一授予许可。未使用 AI 生成图片替代实验截图。

| 保存文件 | 作者/生成方式与证据类型 | 原始来源/版本 | 许可及核对状态 |
|---|---|---|---|
| [assets/episode-000/source-storyboard.png](assets/episode-000/source-storyboard.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000/source-storyboard.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v2/robot-preview.gif](assets/episode-000-v2/robot-preview.gif) | 原工作区实际仿真录像抽帧；动图为 8 倍速概览降采样，非控制速度 | `wbc_demo/umi_replay/media/episode-000-v2/robot-preview.gif`；捕获版本 `5015ce3` | 模型/渲染衍生许可未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v2/robot-storyboard.png](assets/episode-000-v2/robot-storyboard.png) | 原工作区实际仿真录像抽帧；动图为 8 倍速概览降采样，非控制速度 | `wbc_demo/umi_replay/media/episode-000-v2/robot-storyboard.png`；捕获版本 `5015ce3` | 模型/渲染衍生许可未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v2/camera-axis-before-after.png](assets/episode-000-v2/camera-axis-before-after.png) | 原工作区实际 URDF/STL 的旧新 EEF 投影；非实机标定 | `wbc_demo/umi_replay/media/episode-000-v2/camera-axis-before-after.png`；捕获版本 `5015ce3` | 模型衍生许可未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v2/waist-roll-before-after.png](assets/episode-000-v2/waist-roll-before-after.png) | 原工作区实际执行/反馈数据重算的误差、开度或腰部曲线 | `wbc_demo/umi_replay/media/episode-000-v2/waist-roll-before-after.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v2/head-left-frame.png](assets/episode-000-v2/head-left-frame.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v2/head-left-frame.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v2/tracking-summary.png](assets/episode-000-v2/tracking-summary.png) | 原工作区实际执行/反馈数据重算的误差、开度或腰部曲线 | `wbc_demo/umi_replay/media/episode-000-v2/tracking-summary.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v3/quad-middle.png](assets/episode-000-v3/quad-middle.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v3/quad-middle.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v3/web-live-ui.png](assets/episode-000-v3/web-live-ui.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v3/web-live-ui.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v3/tracking-summary.png](assets/episode-000-v3/tracking-summary.png) | 原工作区实际执行/反馈数据重算的误差、开度或腰部曲线 | `wbc_demo/umi_replay/media/episode-000-v3/tracking-summary.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v4/quad-middle.png](assets/episode-000-v4/quad-middle.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v4/quad-middle.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v4/gripper-summary.png](assets/episode-000-v4/gripper-summary.png) | 原工作区实际执行/反馈数据重算的误差、开度或腰部曲线 | `wbc_demo/umi_replay/media/episode-000-v4/gripper-summary.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v4/gripper-endpoints.png](assets/episode-000-v4/gripper-endpoints.png) | 原工作区实际仿真录像抽帧；动图为 8 倍速概览降采样，非控制速度 | `wbc_demo/umi_replay/media/episode-000-v4/gripper-endpoints.png`；捕获版本 `5015ce3` | 模型/渲染衍生许可未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v4/web-before-drag.png](assets/episode-000-v4/web-before-drag.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v4/web-before-drag.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v4/web-after-drag.png](assets/episode-000-v4/web-after-drag.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v4/web-after-drag.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v5/quad-middle.png](assets/episode-000-v5/quad-middle.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v5/quad-middle.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v5/realtime-summary.png](assets/episode-000-v5/realtime-summary.png) | 原工作区实际执行/反馈数据重算的误差、开度或腰部曲线 | `wbc_demo/umi_replay/media/episode-000-v5/realtime-summary.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/episode-000-v6/head_left.mp4](assets/episode-000-v6/head_left.mp4) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v6/head_left.mp4`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v6/quad-middle.png](assets/episode-000-v6/quad-middle.png) | TacVerse 源采集画面与原工作区仿真画面抽帧/拼接/标注；作者身份未知 | `wbc_demo/umi_replay/media/episode-000-v6/quad-middle.png`；捕获版本 `5015ce3` | 源画面及其衍生部分 CC-BY-SA-4.0（继承原说明）；其余模型/渲染部分许可未单独明确；本轮未联网重验 |
| [assets/episode-000-v6/error-decomposition.png](assets/episode-000-v6/error-decomposition.png) | 原工作区实际同步日志重算的诊断图，保留失败与不完整验收边界 | `wbc_demo/umi_replay/media/episode-000-v6/error-decomposition.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/ik-learning-v1/01-fk-ik-jacobian.png](assets/ik-learning-v1/01-fk-ik-jacobian.png) | 原工作区 learning_materials 生成；教学计算/示意，非新运动实验 | `wbc_demo/umi_replay/media/ik-learning-v1/01-fk-ik-jacobian.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/ik-learning-v1/02-numerical-iteration.png](assets/ik-learning-v1/02-numerical-iteration.png) | 原工作区 learning_materials 生成；教学计算/示意，非新运动实验 | `wbc_demo/umi_replay/media/ik-learning-v1/02-numerical-iteration.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/ik-learning-v1/03-v5-control-stack.png](assets/ik-learning-v1/03-v5-control-stack.png) | 原工作区 learning_materials 生成；教学计算/示意，非新运动实验 | `wbc_demo/umi_replay/media/ik-learning-v1/03-v5-control-stack.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/ik-learning-v1/04-v5-tracking-diagnostics.png](assets/ik-learning-v1/04-v5-tracking-diagnostics.png) | 原工作区 learning_materials 生成；旧 v5 日志诊断，非新运动实验 | `wbc_demo/umi_replay/media/ik-learning-v1/04-v5-tracking-diagnostics.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/ik-learning-v1/05-error-decomposition.png](assets/ik-learning-v1/05-error-decomposition.png) | 原工作区 learning_materials 生成；教学计算/示意，非新运动实验 | `wbc_demo/umi_replay/media/ik-learning-v1/05-error-decomposition.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/pinocchio-study-v1/kinematics-comparison.png](assets/pinocchio-study-v1/kinematics-comparison.png) | 旧回放状态的离线 FK/Jacobian 兼容性及耗时计算，非整链路基准 | `wbc_demo/umi_replay/media/pinocchio-study-v1/kinematics-comparison.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/online-ab-pilot-v1/online-comparison.png](assets/online-ab-pilot-v1/online-comparison.png) | 原工作区实际同步日志重算的诊断图，保留失败与不完整验收边界 | `wbc_demo/umi_replay/media/online-ab-pilot-v1/online-comparison.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/online-ab-pilot-v1/episode-001-urdf-r02.png](assets/online-ab-pilot-v1/episode-001-urdf-r02.png) | 原工作区实际同步日志重算的诊断图，保留失败与不完整验收边界 | `wbc_demo/umi_replay/media/online-ab-pilot-v1/episode-001-urdf-r02.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/online-ab-v1/online-comparison.png](assets/online-ab-v1/online-comparison.png) | 原工作区实际同步日志重算的诊断图，保留失败与不完整验收边界 | `wbc_demo/umi_replay/media/online-ab-v1/online-comparison.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/playback-waist-v1/alignment.svg](assets/playback-waist-v1/alignment.svg) | 原工作区生成的共同世界变换教学示意，非硬件标定 | `wbc_demo/umi_replay/media/playback-waist-v1/alignment.svg`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/playback-waist-v1/delivery.png](assets/playback-waist-v1/delivery.png) | 原工作区修复前后各 15 s 静止探针统计，非全程运动验收 | `wbc_demo/umi_replay/media/playback-waist-v1/delivery.png`；捕获版本 `5015ce3` | 未单独明确，不代为授权；本轮未联网重验 |
| [assets/playback-waist-v1/waist-initial.png](assets/playback-waist-v1/waist-initial.png) | URDF FK 骨架与旧运行日志；固定腰新候选未实际执行 | `wbc_demo/umi_replay/media/playback-waist-v1/waist-initial.png`；捕获版本 `5015ce3` | 未单独明确；含模型衍生内容，不代为授权；本轮未联网重验 |

## 外部与未收录资料

<a id="workspace-materials"></a>

文中的 `wbc_demo/`、`source/`、`logs/`、`data/`、`media/` 和环境名均为**原工作区逻辑定位文字**，不是知识库附件路径。历史命令必须在原工程和对应环境中理解与使用，知识库本身不提供机器人控制或训练入口。

| 类别 | 原工作区逻辑定位与获取边界 |
|---|---|
| 实现与配置 | `wbc_demo/run.sh`、`wbc_demo/dual_arm_ik.py`、`wbc_demo/umi_replay/` 的实现/测试/配置，以及 `source/geniesim_ros/`。留在原工程，受访问权限限制；不发布内部代码。 |
| 初版与压力测试证据 | `wbc_demo/logs/final-*`、`stress-native-02/`、`compare-native-final/`、`lab-*` 等报告、连续轨迹和构建日志。未迁入，不能以链接修复宣称重新验收。 |
| 数据与转换结果 | `wbc_demo/data/xtac-umi-g1-block-to-box/`、`wbc_demo/data/converted/`；原数据公开入口见上表，转换产物未迁入。 |
| UMI 早期/更正与 v2–v5 | `wbc_demo/logs/umi-episode-000-*`、`umi-gripper-eef-*`、`umi-upright-*`、`umi-web-*`、`umi-realtime-web-reliable-01/`；原 CSV、报告和完整录像未迁入。 |
| Pinocchio 与在线 A/B | `wbc_demo/logs/wbc-next-stage/`、`wbc-online-ab-20261019-01/`、`wbc-online-controlled-20261019-01/` 的报告、同步 tick 和源码快照。原环境和原始日志只在工作区，不伪造公开下载。 |
| 最新回放与失败 | `wbc_demo/logs/wbc-online-web-20261019-02/`、`wbc-online-web-playback-review/`、`playback-waist-review/`；本包只保存精选媒体和原文定量摘要。 |
| 各媒体完整验收包 | 原工程 `wbc_demo/umi_replay/media/` 的 HTML、JSON/CSV 与其余 MP4，以及 `wbc_demo/logs/umi-evidence-*`；本包各素材页列出实际保留文件。 |
| 模型与运行环境 | CAD、URDF/mesh、USD/MJCF、Kit 扩展缓存、mamba/venv、构建产物、容器和原始剖析记录全部留在原工程或其既有资源位置。 |

未迁入的资源链接已转到本节并标记“工作区资料”；不会让知识库相对链接跳出仓库。文档和精选素材的 SHA256 不能替代这些未随文证据的实际内容。

## 本轮文档与摘编清单

| 源文件逻辑路径 | 本包位置 | 迁入方式 |
|---|---|---|
| `wbc_demo/EXPERIMENT_RESULTS.md` | [topics/wbc/EXPERIMENT_RESULTS.md](topics/wbc/EXPERIMENT_RESULTS.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/LAB_USAGE.md` | [topics/wbc/LAB_USAGE.md](topics/wbc/LAB_USAGE.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/README.md` | [topics/wbc/README.md](topics/wbc/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/REPRODUCTION_LOG.md` | [topics/wbc/REPRODUCTION_LOG.md](topics/wbc/REPRODUCTION_LOG.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/RESULTS.md` | [topics/wbc/RESULTS.md](topics/wbc/RESULTS.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/WHOLE_BODY_IK_GUIDE_ZH.md` | [topics/wbc/WHOLE_BODY_IK_GUIDE_ZH.md](topics/wbc/WHOLE_BODY_IK_GUIDE_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/CODE_AUDIT_ZH.md` | [topics/umi-replay/CODE_AUDIT_ZH.md](topics/umi-replay/CODE_AUDIT_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/COORDINATES_ZH.md` | [topics/umi-replay/COORDINATES_ZH.md](topics/umi-replay/COORDINATES_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/GRIPPER_AND_WEB_FIX_ZH.md` | [topics/umi-replay/GRIPPER_AND_WEB_FIX_ZH.md](topics/umi-replay/GRIPPER_AND_WEB_FIX_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/GRIPPER_EEF_CORRECTION_ZH.md` | [topics/umi-replay/GRIPPER_EEF_CORRECTION_ZH.md](topics/umi-replay/GRIPPER_EEF_CORRECTION_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/IK_LEARNING_GUIDE_ZH.md` | [topics/umi-replay/IK_LEARNING_GUIDE_ZH.md](topics/umi-replay/IK_LEARNING_GUIDE_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/MULTIVIEW_RESULTS_ZH.md` | [topics/umi-replay/MULTIVIEW_RESULTS_ZH.md](topics/umi-replay/MULTIVIEW_RESULTS_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/ONLINE_AB_RESULTS_ZH.md` | [topics/umi-replay/ONLINE_AB_RESULTS_ZH.md](topics/umi-replay/ONLINE_AB_RESULTS_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/ONLINE_IK_AND_VIEWS_ZH.md` | [topics/umi-replay/ONLINE_IK_AND_VIEWS_ZH.md](topics/umi-replay/ONLINE_IK_AND_VIEWS_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/PINOCCHIO_STUDY_ZH.md` | [topics/umi-replay/PINOCCHIO_STUDY_ZH.md](topics/umi-replay/PINOCCHIO_STUDY_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/PLAYBACK_ALIGNMENT_AND_WAIST_ZH.md` | [topics/umi-replay/PLAYBACK_ALIGNMENT_AND_WAIST_ZH.md](topics/umi-replay/PLAYBACK_ALIGNMENT_AND_WAIST_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/README.md` | [topics/umi-replay/README.md](topics/umi-replay/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/REALTIME_REPLAY_ZH.md` | [topics/umi-replay/REALTIME_REPLAY_ZH.md](topics/umi-replay/REALTIME_REPLAY_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/RESULTS_ZH.md` | [topics/umi-replay/RESULTS_ZH.md](topics/umi-replay/RESULTS_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/UMI_REPLAY_GUIDE_ZH.md` | [topics/umi-replay/UMI_REPLAY_GUIDE_ZH.md](topics/umi-replay/UMI_REPLAY_GUIDE_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/USER_FEEDBACK_REVIEW_ZH.md` | [topics/umi-replay/USER_FEEDBACK_REVIEW_ZH.md](topics/umi-replay/USER_FEEDBACK_REVIEW_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/WBC_NEXT_STAGE_ZH.md` | [topics/umi-replay/WBC_NEXT_STAGE_ZH.md](topics/umi-replay/WBC_NEXT_STAGE_ZH.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/WORK_LOG.md` | [topics/umi-replay/WORK_LOG.md](topics/umi-replay/WORK_LOG.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000/README.md` | [assets/episode-000/README.md](assets/episode-000/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000-v2/README.md` | [assets/episode-000-v2/README.md](assets/episode-000-v2/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000-v3/README.md` | [assets/episode-000-v3/README.md](assets/episode-000-v3/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000-v4/README.md` | [assets/episode-000-v4/README.md](assets/episode-000-v4/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000-v5/README.md` | [assets/episode-000-v5/README.md](assets/episode-000-v5/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/episode-000-v6/README.md` | [assets/episode-000-v6/README.md](assets/episode-000-v6/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/ik-learning-v1/README.md` | [assets/ik-learning-v1/README.md](assets/ik-learning-v1/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/pinocchio-study-v1/README.md` | [assets/pinocchio-study-v1/README.md](assets/pinocchio-study-v1/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/online-ab-pilot-v1/README.md` | [assets/online-ab-pilot-v1/README.md](assets/online-ab-pilot-v1/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/online-ab-v1/README.md` | [assets/online-ab-v1/README.md](assets/online-ab-v1/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `wbc_demo/umi_replay/media/playback-waist-v1/README.md` | [assets/playback-waist-v1/README.md](assets/playback-waist-v1/README.md) | 保留历史正文，增加边界与链接/脱敏调整 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/asset_consumption.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/engines.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/newton_quirks.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/ovrtx_sync.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/param_injection_eval.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/perf.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |
| `source/geniesim_ros/src/ros_ws/src/genie_sim_engine/docs/pipeline.md` | [topics/engine-review.md](topics/engine-review.md) | 多源摘编；非原文镜像 |

## 更新记录

- 2026-10-19：首次迁入，建立原版本和迁入哈希、逐项素材来源、许可及未收录边界。
