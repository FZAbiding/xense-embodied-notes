> 历史文档快照：原记录日期 2026-10-12，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](sources.md)。

# 具身操作仿真技术路线调研：银河通用、Sudo 苏度与 Genesis

调研日期：2026-10-12\
关注范围：机械臂与夹爪资产精度、坐标系、网格、URDF/USD/MJCF、命名与顺序、物体生成、相机与触觉、数据采集、执行评估、IK/FK 与控制方式。\
用途：为 Xense/TacCap 资产管理及后续仿真、数采、策略评估提供技术判断依据。

## 1. 主要结论与阅读边界

**这几条路线共同依赖“资产—物理—传感—控制—数据—真实评估”整条链路；选择某种文件格式，不能替代机械参数核对和系统标定。**

本报告采用四种证据标记：

| 标记 | 含义 | 可以据此判断什么 |
|---|---|---|
| **公开实现** | 已读取官方文档、作者代码或原始资产 | 特定版本的字段、接口、文件内容与设计机制 |
| **论文报告** | 论文作者公布的实验和方法 | 该论文设定下的路线与结果，未经本次独立复现 |
| **厂商声明** | 公司发布的介绍、视频说明或新闻稿 | 公司公开表述，不能直接视为第三方验证 |
| **工程建议 / 推断** | 本报告的分析与建议 | 可作为方案或验收起点，不能反推厂商内部实现 |

本次最有价值的结论如下：

1. **银河通用的公开抓取研究可看到跨工具协作。** GraspVLA 的合成数据路线组合了抓取合成、cuRobo 规划、MuJoCo 验证与 Isaac Sim 渲染；具体文件层面的证据见第 3 节。[GraspVLA 论文 §3][s01]
2. **苏度明确公开了仿真训练与逐步视觉闭环的方向，但底层实现披露有限。** 官方招聘页出现 ManiSkill 和物理引擎岗位，能支持其相关研发投入的判断，不能证明 R1 全部运行在某个固定引擎上。[Sudo R1 官方介绍][s02]、[Sudo 官方招聘页][s03]
3. **Genesis 要同时区分公司和开源平台。** Genesis AI 的公司数据路线涉及人类数据；Genesis World 则是可以检查代码的仿真基础设施。开源平台支持某能力，不等于已证明公司生产系统使用了相同配置。[Genesis AI 公司新闻稿][s04]、[Genesis World 官方仓库][s05]
4. **公开示例 URDF 可能服务于规划和演示，而非高精度动力学。** 本次检查到 GraspVLA playground 示例的七个臂 link 使用相同对角惯量；这是该文件的事实，不能推广成其内部生产资产的结论。详见第 3.1 节。[锁定版本的示例 URDF][s06]
5. **几何面数、渲染材质 roughness、接触摩擦是三个独立问题。** 本次实测示例机械臂碰撞网格仅 200–300 面，但没有原始 CAD 对照，不能据此给出毫米级精度结论。
6. **TCP 控制与关节控制通常分属不同层。** 策略可以输出末端位姿增量，执行层通过 IK 或雅可比映射产生关节目标/力矩；评估必须同时记录策略命令与实际执行状态。

### 1.1 对象辨析

- **银河通用 = Galbot / Galaxy General Robotics。** 本报告使用其参与的 GraspVLA 论文及作者链接的开源实现作为具体案例，不将其他公司同名或相近项目归入银河通用。
- **Sudo 苏度**以 `sudo.ai` 的 R1 介绍及招聘页面为主要依据。其官方职位链接显示上海苏度科技有限公司；与其他同名 Sudo Robotics 网站分别处理。
- **Genesis AI**为公司层面；**Genesis World / genesis-world**为本报告检查的开源平台。报告同时覆盖两者，避免把引擎功能直接等同于公司数据配方。
- Galaxea 与 Galbot 不应按中文名称相近合并；Psi-Robot 的 DexGraspVLA 也没有被当作银河通用项目引用。

### 1.2 版本与验证范围

| 对象 | 本次依据 |
|---|---|
| GraspVLA 方法 | arXiv `2505.03233v2`，2025-07-19；当前主仓库及数据发布页另作补充 |
| GraspVLA playground | 提交 `4d3d4b5b4568dbaf27f71390fd71ef170d800f70` |
| GraspVLA 真机客户端 | 提交 `14e32ebd645e6f9a13da39f22dd1c8985fd4c8f9` |
| Genesis World | 官方发布页已列出 `v1.4.4`，对应 `a649105285d30bb9cd3464e753bc5270f3f43d4b`；部分机制参考 v1.4.0 文档及调研时的 latest 文档 |
| Isaac Sim | 调研时官方 latest 文档；涉及旧 API 时明确区分，不将当前 API 套回 2025 年论文环境 |
| ManiSkill | 调研时官方文档页面标注 3.0.1 |

Genesis 最新版本由[官方发布记录][s07]核对。本次执行了资料检索、公开源码阅读、URDF XML 统计、10 个二进制 STL 的面数/包围盒/哈希检查；**没有安装或运行这些仿真平台，没有进行真实机器人测试，也没有独立复现论文成功率。** 文中的接口示意不是本次已执行的示例。

## 2. 厂商与平台路线对照

| 关注项 | 银河通用：以 GraspVLA 为公开样本 | Sudo 苏度：R1 | Genesis AI / Genesis World |
|---|---|---|---|
| 公开技术重点 | 大规模合成动作数据与 VLA 抓取 | 仿真训练、每步观察的操作闭环 | 公司全栈模型与数据；开源多物理仿真平台 |
| 物理与渲染组合 | 论文披露 MuJoCo + Isaac Sim；规划另用 cuRobo | 招聘涉及 ManiSkill、物理引擎；生产组合未确认 | 平台自有求解器体系，另有 IPC 等耦合；渲染涉及 Nyx 等组件 |
| 机器人资产 | 能检查示例 URDF、规划配置和仿真资源 | 未获得可审计的 R1 资产包 | 能检查导入器与示例；不等于公司本体全部资产开放 |
| 质量/质心精度证明 | 示例有数值，未见覆盖全部硬件的逐 link 测量误差证明 | 本次检索未找到公开参数误差报告 | 引擎能读取物性；输入是否实测需资产方证明 |
| 坐标与关节顺序 | 可读 base、EEF、joint_names 等配置 | 内部规范未找到 | 官方有坐标和局部/全局索引文档 |
| 物体 | 论文使用已有物体网格并生成布局/轨迹 | 物体来源与清洗细则未找到 | 可导入 mesh/关节资产；应用方仍需提供生成与验收流程 |
| 视觉 | 公开客户端能检查图像裁剪与传输 | R1 宣称视觉逐步闭环；标定与取图 API 未公开 | 平台有离屏相机、随 link 挂载、批量取图 |
| 触觉 | 本次检查的抓取输入接口未见触觉输入 | 招聘有触觉岗位；R1 是否使用触觉未确认 | 平台有接触力与 taxel 接口；公司另披露触觉采集手套 |
| 数据与评估 | 有论文、数据页和 playground 评估代码 | 有连续演示及公司统计 | 公司披露多来源数据；平台提供记录与训练基础设施 |
| IK / 控制 | 规划使用 cuRobo；真机客户端发送笛卡尔目标 | R1 输出动作表示与底层控制器未公开 | 平台支持 IK、规划、关节位置/速度/力控制等接口 |

表格事实来源分别为[GraspVLA 论文][s01]、[playground][s08]、[真机客户端][s09]、[Sudo R1][s02]、[Sudo 招聘][s03]、[Genesis 仓库][s05]与[公司新闻稿][s04]。表中的“未找到”只描述本次公开检索结果，不表示厂商内部没有这项能力。

### 2.1 银河通用：从公开管线能学到什么

**论文报告：** SynGrasp-1B 使用 240 类、10,680 个物体实例；先形成布局和候选抓取轨迹，做物理验证，再生成随机化视觉观测。其“十亿”是帧规模，不能解释为十亿个独立任务或十亿条成功轨迹。[论文 §3][s01]

**公开实现：** playground 中既有用于规划的 URDF 与碰撞球配置，也有 robosuite/LIBERO 仿真资源；因此需要分别核对“规划模型”和“执行环境”，不能默认两者由一份文件无损产生。[playground 说明][s08]、[规划配置][s10]

**工程启示：** 多工具方案把物理验证与视觉生产分开后，必须明确谁提供权威状态。如果 A 引擎生成物体/关节轨迹、B 引擎只渲染，应逐帧同步姿态和时间；如果 B 引擎重新积分物理，则必须重新确认接触和任务成功。后一种方式不是简单格式转换。

### 2.2 苏度：已公开方向与仍待确认的实现

**厂商声明：** R1 使用仿真数据训练，无真实示教；官方介绍给出 60 分钟连续评估、约 98% 首次尝试成功率、两次尝试内接近 100%，并称动作根据最新观察以 15–25 Hz 闭环更新。[Sudo R1][s02]

**公开线索：** 官方招聘包括 ManiSkill 生态、物理引擎、仿真资产与评测、Sim2Real、数采和触觉方向。[官方招聘][s03]

**推断边界：** 可以判断其重视仿真基础设施和操作闭环；尚不能据此确认 R1 的主引擎、是否采用强化学习教师蒸馏、内部 URDF/USD/MJCF 分工、是否输入触觉、TCP 动作定义或控制环频率。招聘标题是研发方向证据，不能作为部署架构证明。

对接时优先索取：同版本资产包、动作 schema、相机标定与时间同步说明、未剪辑视频对应逐次日志，以及可重复的失败/成功判据。

### 2.3 Genesis：公司数据路线与开源基础设施

**厂商声明：** Genesis AI 的 GENE-26.5 新闻稿描述了仿真系统、灵巧手、带触觉电子皮肤的采集手套，以及第一视角和互联网人类视频。因此不能将该公司的整体数据路线概括成“只有纯仿真训练”。新闻稿中的成本、效率和能力描述属于公司自述。[公司发布的新闻稿][s04]

**公开实现：** Genesis World 仓库提供机器人资产导入、刚体及其他物理求解、渲染、传感、控制与并行环境的基础设施；Nyx 为相关渲染组件，具体可用路径取决于版本、依赖和后端。[官方仓库][s05]、[Nyx 文档][s11]

**工程启示：** 可以用它研究操作、触觉和多环境数采，但要自行补齐任务定义、资产校验、专家策略、数据 schema 和真机评估。演示里的多物理能力不保证任意复杂接触任务都已具有足够精度；性能也必须在相同场景、传感器、求解器精度和硬件条件下比较。

## 3. 机械臂与夹爪模型：如何判断“精确”

### 3.1 公开文件抽查：GraspVLA playground

本节是**本次文件级检查**，范围仅为锁定提交内的 `assets/franka_with_extended_finger/`。它不代表银河通用全部仿真资产，也不代表 SynGrasp-1B 内部生产文件。

| 检查项 | 本次结果 | 判断 |
|---|---|---|
| link / joint 数量 | 27 个 link、26 个 joint | 是 XML 节点统计，不是 26 个可控自由度 |
| 活动关节 | 7 个 revolute + 2 个 prismatic，其余 17 个 fixed | 要另核对导入后自由度及固定 link 合并 |
| 质量字段 | `panda_link1…7` 依次为 2.7、2.73、2.04、2.08、3、1.3、0.2 kg | 字段存在，未找到这些数值的逐项实测误差证明 |
| 臂段惯量 | 七个臂 link 均为 `diag(0.1, 0.1, 0.1)`，交叉项为 0 | 高度简化；不能视为已核准的动力学惯量 |
| 质心字段 | 有 `<inertial><origin>` | 有坐标值不等于已通过质心测量 |
| 部分无惯性 link | 如 `panda_hand`、`eef_link` 等 | 需要区分实体零件和虚拟 frame；不能把每个缺失都判成错误 |
| 两个移动指 | 两个 prismatic，文件未声明 `<mimic>` | 不能声称此 URDF 自带单驱动同步耦合 |
| TCP 候选 | 有 `eef_link` 等多个末端 frame | 必须按消费端配置确认实际控制点 |

以上直接来自[锁定版本 URDF][s06]。相同惯量是可核查事实；“高度简化”是本报告判断，不能进一步断言数值由谁估算，或内部仿真一定采用这些值。

规划配置还显式记录 `base_link`、`ee_link`、`cspace.joint_names`、锁定夹爪关节、碰撞球及缓冲，但含作者机器上的 作者本机绝对目录（路径未随文发布）。[锁定版本 franka.yml][s10]

这意味着它是可研究的示例入口，交付到 Xense 资产目录时还要重新设计可搬移路径、来源与参数核对流程。这里的碰撞球缓冲也不能直接复制为其他机械臂的安全距离。

### 3.2 精度应分成六个验收层

以下为**工程建议**，并非某厂商内部标准。

| 层级 | 验收对象 | 推荐证据 | 单独通过后不能证明什么 |
|---|---|---|---|
| 结构 | link 树、左右结构、关节耦合、型号 | 官方结构图/CAD/锁定源文件 | 轴向、零位与硬件一致 |
| 运动学 | joint origin、axis、零位、限位、TCP | 厂商手册与多姿态实测 | 动力学与接触精度 |
| 几何 | 长度、形状、孔位、指尖轮廓 | CAD 对比、尺寸测量 | 质量、摩擦与内部材料 |
| 刚体动力学 | mass、COM、inertia、载荷 | 原厂物性、CAD 材料/BOM、辨识 | 表面接触与柔性响应 |
| 执行器 | 增益、阻尼、饱和、延迟、死区 | 关节响应与跟踪实验 | 视觉和触觉标定 |
| 接触与传感 | 摩擦、柔顺、胶体、相机、触觉 | 专项标定和独立测试 | 新工况下自动准确 |

对抓取视觉策略，关节轴、TCP、指尖形状和相机外参往往先影响可用性；对高速动作、力控制、插接与触觉操作，惯性、执行器和接触参数的影响会显著增加。这是任务敏感性判断，不能作为省略质量/惯量记录的理由。

### 3.3 质量、质心和惯量的获取与检查

建议按“原厂可追溯数据 → 有材料/BOM 的 CAD 物性 → 实物测量/系统辨识”的路径获取。只有外表面 STL 时，通常不能确定电机、减速器、空腔和配重的分布；不得直接默认均匀实体后把结果写成实测参数。

需要检查：

- 单位：质量 kg，质心 m，惯量 kg·m²；CAD 导出单位和 URDF mesh scale 都要记录。
- 原点：URDF 惯性 origin 表达质心相对 link 的位置，惯量还关联惯性坐标轴；不能把 CAD 装配原点直接当质心。
- 数学一致性：惯量矩阵对称、物理实体的主惯量合理；对正质量三维刚体检查正定性及主惯量三角不等式，退化几何另作说明。
- 总量一致性：分 link 质量之和与整机称重、附件和载荷范围相符；虚拟 frame 不应为了消除警告随意加质量。
- 固定件合并：合并时要做坐标旋转与平行轴变换，不能直接逐项相加不同坐标系的惯量。
- 左右镜像：反射不是刚体旋转；左右手应依据各自来源核对轴向、限位、质心与惯量交叉项。

惯量换算可用下式核对。设 `R` 把质心惯性轴转到目标轴，`d` 为目标原点到质心的向量，且都在目标坐标系表达：

```text
I_target_origin = R I_COM Rᵀ + m [(dᵀd) I₃ − d dᵀ]
```

这是刚体惯量换算关系，不是从网格反推真实质量的依据。缺失值保留为“未知/待核对”；后续训练随机化的范围独立保存，并标明依据。

### 3.4 夹爪特别容易遗漏的内容

平行夹爪要明确“开口宽度”与“单指位移”的关系。只有对称、两指各运动一半时才有 `width = 2 × finger_travel`；不同零位、偏置和传动结构不能套用此式。

欠驱动或连杆夹爪还需区分：驱动关节、从动关节、闭链约束、机械联动和控制同步。URDF 的线性 mimic 关系可表达部分耦合，但不能完整代表所有非线性连杆运动和接触力传递。

触觉胶体、保护套、相机和转接件既会改变外形/TCP，也可能改变质量、惯量、刚度和有效夹持宽度。应按可追溯附件配置管理，避免只修改可视 mesh。

## 4. 坐标系、link/joint 命名和排列顺序

### 4.1 坐标约定：先写清变换的方向

ROS REP-103 采用 SI、右手系；常见本体轴为 X 前、Y 左、Z 上，相机 optical frame 为 Z 前、X 右、Y 下。这是 ROS 约定，不能据此改写厂商源模型的轴。[REP-103 官方原文][s12]

建议对新装配显式列出以下 frame，名称是**示例公司约定**：

```text
world
└─ platform_base
   ├─ left_arm_base → … → left_flange → left_tool_mount → left_tcp
   │                                             └─ left_wrist_camera_link
   │                                                  └─ left_wrist_camera_optical
   ├─ right_arm_base → … → right_flange → right_tool_mount → right_tcp
   └─ head_yaw → head_pitch → head_camera_link → head_camera_optical
```

本文约定 `T_A_B` 把 B 坐标表达转换到 A 坐标表达，即 `p_A = T_A_B p_B`。因此：

```text
T_world_tcp = T_world_base · FK_base_flange(q) · T_flange_tcp
T_world_wristcam = T_world_flange(q) · T_flange_wristcam
T_world_headcam = T_world_head(q_head) · T_head_headcam
```

固定外部相机的世界外参可为常量；腕部、转动头部相机随关节状态变化。若图像元数据要保存外参，必须记录曝光时对应的状态，不能只写初始安装值。

### 4.2 三类不能混用的轴与角度

| 项目 | 需要核对的区别 |
|---|---|
| joint axis | 在关节局部坐标中定义，不能只看世界坐标方向 |
| mesh 坐标 | CAD/网格局部原点与 link frame 可能不同，依靠 visual/collision origin 对齐 |
| camera 坐标 | ROS optical、渲染器 camera 与 look-at/up 约定可能不同 |
| 四元数 | 必须声明 `xyzw` 或 `wxyz`；顺序交换不是坐标变换 |
| 欧拉角 | 必须声明轴序、内/外旋、角度单位；URDF RPY 与某些 API 的 degree 参数不能直接互传 |
| USD stage | `upAxis`、`metersPerUnit` 以及对象局部变换必须共同检查 |

Genesis 文档明确右手 Z-up、四元数 `wxyz`，其部分欧拉角接口使用 degree；这与 URDF RPY 的 rad 需要适配。[Genesis 坐标与单位约定][s13]

**推荐验收方法：** 在 viewer 中显示 base、各 joint、TCP、相机与触觉轴；对每个独立关节施加小正增量；对 TCP 的 X/Y/Z 正向平移和三个正向旋转逐项验证；用已知空间点检查相机投影。动画看起来正常，不能替代这些方向检查。

### 4.3 命名：保留上游，实例化时加前缀

本次检索未发现三家公司共同发布的 link/joint 命名及顺序标准。建议延续 xense-description 现有规则：

1. 部件内部保留上游名称，来源快照不可改写。
2. 装配时添加 `left_`、`right_` 或稳定实例前缀，同时处理 joint、link、mimic、material 的引用。
3. 对 TCP、法兰、相机和触觉 frame 提供显式语义映射，避免消费端猜名字。
4. 将源名称与 USD prim path、MJCF body/joint/site 名称形成可导出的映射表。
5. 若目标格式不能保留原名称，记录可逆映射并检查重名冲突。

Isaac Sim 导入文档说明某些不符合 prim 名称约定的字符会被替换。这一机制意味着“导入成功”仍可能改变名称，需检查映射。[Isaac Sim URDF 导入器][s14]

### 4.4 顺序：至少维护四套清单

| 顺序 | 含义 | 是否可直接替代其他顺序 |
|---|---|---|
| XML 出现顺序 | 文件中元素的书写顺序 | 不可当作通用控制协议 |
| 运动学树顺序 | 从 root 遍历的父子关系 | 分支顺序依解析器/遍历策略 |
| 仿真状态顺序 | 引擎 qpos、DOF、joint 数组的索引 | 固定合并、自由关节和解析选项会影响 |
| 策略/硬件顺序 | 数据集动作、模型输出、电机命令顺序 | 必须由显式名称列表定义 |

Genesis 特别区分 entity-local 与 solver-global 索引：第二台机械臂的全局索引一般不同于它自己的局部索引。[Genesis 命名与索引][s15]

建议适配器在启动时输出并核对 `joint_names`、独立驱动 joint 清单、`qpos` 地址、DOF 地址、动作维度与硬件顺序。不能用字符串字典序排序，例如 `joint10` 可能排在 `joint2` 前；也不能默认浮动基座的配置变量数等于速度 DOF 数。

```text
policy_action[k]
  → explicit_action_joint_names[k]
  → joint_name_to_engine_dof
  → engine_command[dof]
  → measured_state 按同一名称映射回数据集
```

夹爪只有一个独立动作时，从动关节的状态仍可记录，但不能无意把从动 joint 作为第二个独立电机输出。

## 5. STL 三角面片、外观粗糙度与碰撞几何

### 5.1 “粗糙程度”的三个含义

| 含义 | 影响 | 应如何记录 |
|---|---|---|
| 网格离散误差 | 轮廓、孔位、局部曲率、接触表面逼近 | 相对 CAD/扫描的距离、法向误差、面数和单位 |
| PBR roughness | 光反射、镜面高光、图像域差异 | 材质参数/纹理及渲染器版本 |
| 接触表面特性 | 滑移、夹持、滚动、胶体接触 | 摩擦、刚度/阻尼等经过标定的物理参数 |

普通 STL 主要保存三角形几何，不自带可靠的材质、单位或摩擦定义。细分同一个平面会增加三角面数，却不增加几何信息；平滑法线或 roughness 纹理也不改变实际碰撞形状。

### 5.2 本次实际统计：公开示例网格

以下来自同一锁定提交。方法为读取二进制 STL 的面数、校验字节长度 `84 + 50 × N`，并遍历顶点计算包围盒。

| STL 文件 | 三角面数 | 顶点坐标包围盒尺寸 X×Y×Z，按该模型 m 解释 |
|---|---:|---|
| `robot_arm/link0.stl` | 200 | 0.225646 × 0.189284 × 0.140035 |
| `robot_arm/link1.stl` | 300 | 0.110148 × 0.184565 × 0.246977 |
| `robot_arm/link2.stl` | 300 | 0.110138 × 0.249230 × 0.184586 |
| `robot_arm/link3.stl` | 300 | 0.192207 × 0.166120 × 0.176174 |
| `robot_arm/link4.stl` | 300 | 0.192746 × 0.179159 × 0.166259 |
| `robot_arm/link5.stl` | 300 | 0.110100 × 0.185032 × 0.316723 |
| `robot_arm/link6.stl` | 200 | 0.180213 × 0.133069 × 0.100294 |
| `robot_arm/link7.stl` | 200 | 0.125341 × 0.125217 × 0.054847 |
| `customized_gripper/finger_link1_1.STL` | 804 | 0.019000 × 0.021000 × 0.024000 |
| `customized_gripper/basebody2_link.STL` | 22,836 | 0.057197 × 0.205589 × 0.080500 |

网格位置见[锁定版本 mesh 目录][s16]；URDF 将上述臂网格用于 collision。**这不是对 CAD 几何误差、表面加工粗糙度或实际碰撞性能的测量。** STL 本身不声明 m；这里的单位解释来自模型上下文，未做实物尺寸复核。未检查所有 mesh 的水密性、薄壁、退化三角形或接触稳定性。

能得出的结论是：同一公开资产包的网格复杂度差别很大；不能以某个统一面数判断全部资产是否适合仿真。

### 5.3 建议维护 visual 与 collision 两套派生

- **visual**：保存轮廓、颜色、PBR、透明件及相机视域内的重要细节；可采用 OBJ/GLB/USD 等带材质资源。
- **collision**：优先使用任务所需的简单几何或凸分解；重点保护指尖、凹槽、杯口、孔与插接表面。
- **触觉几何**：还需核对触觉模型实际查询的 collision、SDF 或点云；不能只看渲染 mesh。

Genesis 网格处理文档明确区分可视与碰撞用途，并提供简化、凸分解、SDF 等路径及缓存机制。[Genesis mesh processing][s17]

MuJoCo 的常规 mesh 碰撞路径涉及凸几何处理；复杂凹形物体不能仅凭其渲染外观判断是否保留凹面，需使用适合所选版本的凸分解、SDF 或其他碰撞表示。[MuJoCo mesh 参考][s18]

**工程建议：** 用“几何偏差 + 接触任务 + 性能预算”决定网格级别，不规定所有模型统一 N 面。对每个派生保存原件哈希、转换工具版本、参数、缩放和误差报告。若要设毫米级门槛，应先按目标任务建立误差预算；本次没有足够证据给三家公司指定相同的面数或精度标准。

## 6. URDF / USD / MJCF：格式选择与标准制定

### 6.1 三种格式各自负责什么

| 格式 | 适合承担的角色 | 需要补充的内容 |
|---|---|---|
| URDF / Xacro | 机器人结构、关节、几何引用、基础惯性；ROS 与规划生态入口 | 完整接触、执行器、传感器与任务通常还需要其他配置 |
| MJCF | MuJoCo 原生的 body/joint/geom、actuator、sensor、equality 等动力学场景 | 与其他引擎的字段语义映射、外观资源、分发规范 |
| USD / OpenUSD | 场景组合、层、实例、材质、相机，以及物理 schema | 实际物理后端、扩展 schema、导入器和版本兼容性 |
| STL / OBJ / GLB 等 | 几何或带材质网格载体 | 不能独立定义完整机器人、关节协议和标定 |

MJCF 的 body 层级语义与 URDF 的 parent/child joint 图不同；不能简单按 XML 标签一一替换。[MuJoCo modeling][s19]

USD 的 UsdPhysics 定义公共物理 schema，但引擎特有的材料、驱动和接触设置仍要检查。[OpenUSD 物理 schema][s20]

**版本提醒：** 当前 MuJoCo 官方也提供实验性 OpenUSD 支持，不能再笼统写成“MuJoCo 只能读取 MJCF/URDF”；实验性支持也不表示所有 USD 字段无损互通。[MuJoCo OpenUSD 状态][s21]

### 6.2 对 Xense 的建议分工

当前遵循仓库既有 v1 资产机制，优先维护可追溯的 URDF 与 mesh，不要求每项资产同时维护三种可独立编辑的文件。

```text
锁定的厂商输入 / CAD / 原始模型
        ↓ 保留原件、单位、许可证、哈希、核对状态
资产入口：authoring 指定唯一权威来源 + asset.json
        ├─ URDF + 资源：当前交付、viewer、规划入口
        ├─ MJCF 派生：消费端需要时生成并验证
        └─ USD 派生：消费端需要时生成并验证

平台控制器、接触参数、传感器运行配置、任务与数采逻辑
        → 位于各自仿真/控制/数据仓库，引用资产 ID 与版本
```

“唯一权威来源”可能是上游 URDF、Xacro/config、已有 MJCF 或有记录的 STEP 派生；应由 `authoring` 明确，不能强行将所有资产都转成手写 URDF 后丢弃来源。

### 6.3 标准应分四层，避免把内部规则说成行业标准

| 层 | 已有机制 / 建议 | 交付物 |
|---|---|---|
| 文件语法 | URDF、MJCF、OpenUSD 各自格式 | 可解析文件与依赖 |
| 坐标与单位 | 参考 REP-103、目标平台约定 | frame/单位/旋转约定表 |
| 公司资产规范 | 现有 asset.json v1、稳定 ID、来源与入口 | 资产目录与 schema 校验 |
| 仿真/数采语义 | 建议另建带版本的消费协议 | joint/action/observation/calibration 映射与验收结果 |

后三者不能仅凭文件扩展名自动满足。新增消费协议是本报告建议，不表示本仓库已经实现这些字段。

### 6.4 转换后必须检查的语义

| 项目 | 常见变化 | 验证方法 |
|---|---|---|
| 长度与世界轴 | mm↔m、Y-up↔Z-up、局部变换烘焙 | 包围盒、基准点、frame 对比 |
| 固定 link | 合并、层级变化、frame 丢失 | 语义 frame 表与质量/惯量聚合检查 |
| 惯性 | 自动估算、重定位或主轴表示 | 还原到共同坐标系比较 |
| mimic/闭链 | 忽略、变成引擎约束、运行时不支持 | 全开合扫描、驱动数与约束检查 |
| collision | visual 自动生成、凸包封孔、分解变化 | 显示 collider 并做接触任务 |
| 执行器 | URDF limit 与驱动饱和/增益不同 | 响应测试与实际力矩记录 |
| 名称和索引 | prim 名称替换、joint 重排 | 显式名称映射与单 joint 检查 |
| 路径 | 本机绝对路径、未解析 package URI、纹理丢失 | ZIP 解压搬移、必要时 ROS share 安装 |

**当前版本变化尤其需要关注：** 调研时 Isaac Sim latest 导入文档已说明 Newton 相关 articulation/mimic schema 与旧 PhysX 路径的区别。因此不能把旧教程的导入器参数和 schema 复制为所有版本的通用答案。[当前 Isaac Sim URDF 导入文档][s14]

本次只调研这些变化，没有对 Xense 资产执行 URDF→USD/MJCF 转换或跨引擎回归。

## 7. 机器人如何进入仿真，操作物体如何生成

### 7.1 加载机器人后，还缺哪些运行信息

以下是**建议的系统分层**，用于解释模型如何被使用，不代表三家内部采用完全相同的实现。

| 阶段 | 输入 | 形成的运行对象 / 工作 |
|---|---|---|
| 资产解析 | URDF/MJCF/USD、mesh、材质 | link、joint、collider、惯性与层级 |
| 机器人实例化 | 基座固定/浮动、装配关系、初始 q | articulation 与运行状态 |
| 物理配置 | 时间步、重力、求解器、接触材料 | 能进行动力学积分的场景 |
| 执行器配置 | 驱动方式、增益、饱和、延迟 | 从动作到实际关节运动的模型 |
| 传感器配置 | 相机、触觉布局、噪声、时间戳 | 策略可读取的观测 |
| 任务配置 | 目标物体、初始分布、终止条件 | 可重置、可评价的环境 |
| 数采 / 评测 | 专家/策略、版本、记录协议 | episode、训练样本、评估结果 |

Genesis 通过 morph 向 scene 添加机器人或物体，支持 URDF、MJCF、mesh、USD 等入口；“可以加载”是解析能力，不是输入参数已准确。[Genesis 资产加载][s22]

ManiSkill 的 GPU 路线依托 SAPIEN/PhysX 管理多环境状态与渲染。它可作为苏度招聘方向所对应的公开技术生态参考，但不能当作 R1 架构已经公开的证明。[ManiSkill GPU 仿真机制][s23]

### 7.2 物体生成至少包含三件不同的事

1. **物体资产生成/获取**：获取几何、纹理、结构。
2. **物理资产准备**：补充经过确认的碰撞、质量、惯性、关节与材料配置。
3. **任务实例生成**：采样对象、位置、姿态、布局、指令、障碍和目标条件。

已有 mesh 数据库、程序化建模、扫描重建、CAD、图像/文本到 3D 都可能提供第一步。Objaverse 提供大量 3D 资源；不能因此假定下载的每个物体都具备真实尺度与经过标定的接触参数。[Objaverse 官方项目][s24]

**工程建议：** 对生成式物体，先排除破面、自交、异常尺度、不可抓取几何和纹理缺失；再判断是否需要中空结构、可动关节、柔性或液体。只适合视觉训练的资产可以明确标记用途，不应自动成为接触训练资产。

### 7.3 建议的物体与场景生产流程

```text
来源与授权检查
 → 几何/材质清洗、单位确认
 → visual/collision 及语义部件准备
 → 物性来源核对，未知量单独标记
 → 物理稳定性与关键接触测试
 → 初始状态/物体组合/障碍随机化
 → 专家策略或规划器尝试
 → 成功判据筛选与失败标签
 → 状态回放、视觉/触觉采集
 → 数据完整性检查与训练/测试划分
```

场景随机放置后，可用物理落稳生成合理接触关系；不能把“停止移动”直接等同于有效布局，还需检查穿透、可达性、遮挡、桌面边缘和任务是否可解。

### 7.4 刚体、关节物体、柔性物体应分别建模

| 物体类型 | 必要补充 | 典型误区 |
|---|---|---|
| 杯、盒、瓶等刚体 | 中空碰撞、接触面、质量/重心 | 凸包封闭杯口，渲染有洞而物理没洞 |
| 抽屉、门、剪刀等关节物体 | joint origin/axis、限位、阻尼、把手 frame | 只有整体 mesh，没有可动结构 |
| 布、软包、胶体等柔性物体 | 体/壳离散、材料与边界条件 | 使用刚体近似却宣称已验证变形 |
| 含液体或颗粒 | 对应求解器与耦合、初始化与数值设置 | 从照片真实推断流动真实 |

Genesis 的多物理能力提供候选工具；具体对象需要的离散方式和材料仍需验证。尤其柔体的网格分辨率会影响数值行为，不能只把刚体 STL 面数策略原样套用。

### 7.5 随机化的正确位置

建议将参数分为：

- **已标定名义值**：真实系统当前最佳估计，保留来源与误差。
- **不确定性范围**：来自设备差异、测量或实验依据，用于训练随机化。
- **压力测试范围**：刻意超出常规使用条件，单独标记，观察失效边界。

视觉可随机化光照、背景、材质、相机微扰与噪声；动力学可研究质量、摩擦、执行延迟、增益等变化。但未知物性不能仅靠随意随机化被“补成准确”。对质量、惯性和密度的联合随机化还应保持物理一致性。

## 8. 腕部相机、头部相机与仿真图像获取

### 8.1 腕部、头部和固定相机的作用

| 相机位置 | 主要价值 | 需要验证的问题 |
|---|---|---|
| 腕部 | 接近物体、指尖附近细节、随抓取姿态变化 | 手眼标定、末端遮挡、近距离成像、运动模糊 |
| 头部 | 全局任务与双臂工作区观察 | 头部关节状态、俯仰/偏航链路、双臂遮挡 |
| 固定外部 | 稳定视角、跨 episode 对齐 | 基座到相机外参、安装变化、环境覆盖 |
| 双目 / 多目 | 几何信息与遮挡补偿 | 内参、相对外参、同步及左右图顺序 |

**厂商公开证据应逐系统理解：** GraspVLA 真机客户端默认配置为 front/side 两台 RGB 相机，不能直接称为“银河通用统一采用头部+腕部”。论文另报告过腕部视角适配实验，也不能把它解释为所有本体的默认配置。[真机客户端说明][s09]、[论文附录 D][s01]

Sudo R1 本次未获得相机完整安装外参、内参和同步接口；Genesis World 可将相机挂在任意合适的移动 link 上。这一平台能力不披露 Genesis 公司机器人实际用了哪组相机。[Genesis camera sensors][s25]

### 8.2 一台可复现的仿真相机需要什么配置

**工程建议：** 每个相机实例至少记录：

| 字段组 | 内容 |
|---|---|
| 身份与挂载 | camera ID、parent frame、安装变换、实体版本 |
| 成像几何 | 分辨率、fx/fy/cx/cy、投影模型、畸变、near/far |
| 图像含义 | RGB/BGR/RGBA、dtype、范围、通道、深度含义与单位 |
| 采样时间 | 曝光时间、帧时间戳、采样率、延迟、丢帧、同步方式 |
| 图像处理 | crop、resize、undistort、内参更新方法 |
| 随机化 | 名义值、扰动范围、episode 实际采样值、种子 |

如果用 FOV 代替内参，要明确是水平还是垂直 FOV。无畸变针孔模型下，垂直方向有 `fy = H / (2 tan(vFOV/2))`；不能将水平角直接塞进垂直 FOV 参数。

若先在原图裁剪 `(x0, y0)`，再分别以 `sx, sy` 缩放：

```text
fx' = sx·fx      fy' = sy·fy
cx' = sx·(cx−x0) cy' = sy·(cy−y0)
```

因此数据集必须绑定处理后的内参，不能只保存相机出厂 K 矩阵。对有畸变或复杂重采样的流程，还要保存具体映射而非仅依赖此式。

### 8.3 银河通用公开客户端：图像到底怎么进模型

**代码阅读结果：** 相机包装器以 30 FPS 初始化，接收 640×480 图像，中心裁成 480×480 再缩放至 256×256；模型请求传入前/侧 RGB 和末端本体状态。尽管相机接口取到 depth，此包装器返回模型的是 RGB。[锁定版本 cameras.py][s26]、[grasp_mode.py][s27]

这说明“用了 RealSense”不等于“策略一定输入 RGB-D”。相机采样率、模型推理频率与底层关节伺服频率也必须分别报告。

### 8.4 Genesis：直接取离屏图像，不依赖 GUI 截图

调研时文档区分了两条接口：

| 接口 | 文档描述的用途 |
|---|---|
| `scene.add_sensor(...)` → `camera.read().rgb` | 通过传感器接口读取 RGB tensor；可挂载 link |
| `scene.add_camera()` → `render(...)` | 可视化相机按需输出颜色、深度、分割和法线等通道 |

传感器 RGB 的形状为 `([n_envs,] H, W, 3)`，而分辨率配置采用 `(W, H)`。深度等通道不能无依据地从 RGB sensor 返回对象中读取。[Genesis 相机接口文档][s25]

挂载时通过运行时名称查到目标 link 的局部索引，再设置相机与 link 的安装变换。不要把教程里的 `link_idx_local=0` 当作腕部固定编号。是否能批量渲染、返回哪些通道，要按选择的后端核对。

### 8.5 Isaac Sim：相机 prim、render product 与数据缓冲

当前官方推荐路径包括 `RtxCamera` 配置相机、`CameraSensor` 管理 annotator，数据通过 `get_data("rgb")` 等读取；返回值含缓冲和信息，多相机可选 `TiledCameraSensor`。深度还区分 `distance_to_camera` 与 `distance_to_image_plane`。[Isaac Sim Camera Sensors][s28]

旧教程中的 `Camera.get_rgba()` 等接口不宜作为无版本示例直接复制。迁移时同时核对相机 tick、渲染推进、CPU/GPU 缓冲、时间戳以及 ROS 发布机制。[官方相机迁移说明][s29]

这一节描述调研时平台能力，不表示 GraspVLA 的历史数据生产环境使用了最新 API。

### 8.6 ManiSkill：观测相机与展示相机有区别

ManiSkill 文档将策略 sensors、human render cameras 和 GUI viewer camera 分开；相机可输出 RGB、depth、position、segmentation 等，具体取决于配置和 shader。[ManiSkill Sensors / Cameras][s30]

训练/评测应读取环境观测里的传感器数据；不能用展示相机录像替代策略输入。若记录视频，需注明它是实际输入画面还是仅用于审阅的视角。

### 8.7 相机标定与同步的建议验收

1. **几何对齐**：多个已知空间点在仿真与实机图像中的投影误差。
2. **手眼一致性**：多个腕部姿态下重新投影同一目标，排除单姿态凑合对齐。
3. **动态同步**：记录曝光/采样时间与对应 q；评估机器人运动时的错位。
4. **处理链对齐**：RGB 顺序、裁剪缩放、深度单位、畸变和归一化一致。
5. **泛化评测**：单独测相机偏移与重新安装，不把外参错误隐藏在总成功率中。

几何误差与时间误差可联合影响投影。例如 0.5 m/s 的运动在 20 ms 时间错位下产生约 10 mm 的位置偏差；这是说明量级的算例，不是任一厂商设备的实测值。

## 9. 触觉、接触力和其他传感数据如何获取

### 9.1 首先区分四种不同数据

| 数据 | 来源 | 能表达什么 | 不能自动代表什么 |
|---|---|---|---|
| 接触点/接触冲量 | 物理求解器 | 引擎实际处理的接触 | 真实传感器原始信号 |
| link 净接触力 / joint effort | 求解器或执行器状态 | link/关节层面相互作用 | 密集触觉分布、完整腕部六维力传感 |
| taxel 阵列 | 几何查询或专门触觉模型 | 局部深度、力估计、标记位移等 | 未经标定的真实压力/剪切力 |
| 视触觉 RGB / 胶体形变 | 胶体+光学近似或物理模型 | 触觉图像与特征 | 真实胶体的全部动力学 |

完整六维腕力还需定义采样点、力矩参考原点、坐标系及是否包含重力、惯性与内部约束反力。只返回三个净接触力分量的 API 不等价于六维力传感器。

### 9.2 Genesis：接触力和 taxel 的依据不同

Genesis 的 `Contact`、`ContactForce`、`JointTorque` 从刚体求解器读取；文档中的 `ContactForce` 是 link 局部系净接触力向量。[Genesis 接触与力传感器][s31]

其 taxel 系列主要根据 SDF 或采样点云估计接触几何；官方明确这些读取是近似且未标定的信号。主要接口如下：[Genesis 触觉文档][s32]

| 类型 | 返回内容 | 文档单位 / 形状要点 |
|---|---|---|
| `ContactProbe` | 各 probe 接触状态 | bool |
| `ContactDepthProbe` | 各 probe 深度 | m |
| `KinematicTaxel` | 各 taxel 力与力矩估计 | link-local，N / N·m |
| `ElastomerTaxel` | 各 marker 位移 | link-local，m |
| `ProximityTaxel` | 近接触力与力矩估计 | link-local，N / N·m |

布局用 link 局部位置描述，创建传感器并推进场景后，通过 `read()` 获取 tensor。**数值标注为 N，并不等于已经与真实 Xense 传感器完成标定。** 还要检查力估计是否反馈进物理求解器，避免把观察近似当成新的真实接触约束。

### 9.3 视触觉路线与 Isaac 平台能力

TACTO 是视触觉渲染的公开参考，支持触觉 RGB/depth 与物理引擎集成；其作者也明确它并不旨在独立提供精确接触动力学。该仓库已归档，实际使用需评估维护与兼容性。[TACTO 官方仓库][s33]

当前 Isaac Sim 资产目录也列出特定触觉数字孪生模块。因此不应笼统认为 Isaac 完全没有触觉支持；是否覆盖 Xense/TacCap，需要检查具体传感器模型、输出机制和标定，不能从资产目录推导通用兼容。[Isaac Sim Tactile Sensors][s34]

### 9.4 对 Xense/TacCap 的具体建议

建议将传感器管理分为两层：

- **资产层**：外壳与胶体几何、安装接口、左右变体、来源、坐标和可确认物性；继续使用现有统一资产机制。
- **仿真/数采层**：taxel/marker 布局、光学模型、采样率、噪声、标定、读数转换与记录代码；放在相应消费仓库。

触觉仿真验收至少做四组实验：

| 实验 | 核对内容 |
|---|---|
| 平面法向加载/卸载 | 深度、法向力、迟滞、饱和与回零 |
| 球/边缘压入 | 接触面积、空间分辨率、边缘响应 |
| 带法向载荷的切向滑移 | 剪切、滑移起点、标记流与摩擦关系 |
| 不同速度与重复循环 | 动态延迟、黏弹、漂移与重复性 |

至少同步记录真机原始图像/原始电信号、参考力、位移和时间，再与仿真输出比较。胶体厚度、材料、照明、相机及解码算法的版本都可能影响读数。

本次没有对三家公司的真实触觉硬件进行测试，也未取得可证明 Xense 传感器已适配其平台的接口或标定包。

## 10. 具身数据集如何采集与组织

### 10.1 四种可组合的数据路线

| 路线 | 采集方式 | 主要价值 | 主要偏差 |
|---|---|---|---|
| 规划/脚本专家 | IK、抓取候选、运动规划和状态机 | 易规模化、动作可解释、真值易获得 | 专家覆盖有限、可能过于理想 |
| 强化学习专家 | 在仿真中优化策略，必要时转为视觉策略 | 可探索接触与恢复行为 | 奖励漏洞、仿真过拟合、稳定性 |
| 遥操作/手套/UMI | 人类示教采集动作与多模态数据 | 复杂任务、多样策略、人类经验 | 标定、重定向、延迟与人员差异 |
| 人类视频与生成增强 | 视频、重建、重定向或视觉增强 | 扩大语义与场景覆盖 | 物理动作与机器人可执行性不直接已知 |

Genesis 公司的混合数据声明与开源引擎接口分别属于公司级和平台级证据。对苏度，可以确认 R1 发布材料的仿真训练声明，不能由此断言公司所有后续任务都不用真实数据。

### 10.2 一条建议的 episode 记录协议

以下是**建议字段**，不是三家公司已公布的共同 schema，也不表示应立刻加入本仓库 `asset.json`。

| 类别 | 建议字段 |
|---|---|
| 复现依据 | episode ID、task ID、seed、数据 schema 版本、平台版本、模型/配置哈希 |
| 资产 | robot/gripper/object asset ID 与 revision、入口、装配和 collider 派生版本 |
| 状态 | 按名称排列的 q/dq、实际 TCP pose、夹爪宽度、必要时力矩和物体状态 |
| 图像 | 各 camera ID 的原始/处理后图像、K、畸变、挂载、每帧外参/时间 |
| 触觉 | 原始读数、解码信号、taxel/marker 顺序、frame、单位、标定版本 |
| 动作 | 策略原始输出、反归一化值、限幅后命令、控制模式、执行时间与反馈 |
| 语言 | 原指令、规范化指令、目标 object ID、必要时动作阶段 |
| 结果 | success、terminated、truncated、失败原因、重试次数、人工干预 |

要区分 `observation_t`、`action_t` 和执行后的 `observation_t+1`。若采用异步渲染/写盘，不能只依赖文件名顺序匹配它们。

```text
示意时序：
t_obs：传感器采样 → 组装观测
t_infer：策略推理 → 输出动作/动作块
t_apply：执行器开始采用命令
t_next：取得下一次可用观测

记录四者时间戳、实际延迟、执行了哪些动作及取消情况。
```

记录器时序也依平台而异：Genesis 文档说明其 recorder 在每次 `scene.step()` 之前采样，此时样本对应该步开始状态与输入。[Genesis Recording data][s35]

ManiSkill 提供 `RecordEpisode` 记录轨迹与视频，相关数据可用于重放/转换；实际需要哪些观测和控制语义仍要配置。[ManiSkill Recording Episodes][s36]

### 10.3 数据质量与划分

建议在扩大规模前验收：图像是否空帧/旧帧、轨迹是否越限、目标是否正确、传感器是否对齐、成功是否只是附着/穿透造成、日志是否能重放。

训练/验证/测试应按**物体实例、物体类别、场景、相机配置或硬件配置**隔离。把一条轨迹的相邻帧随机分入训练和测试，会严重夸大泛化能力。

同时报告 episode 数、独立物体数、任务数、总时长、采样率与有效帧数。相同轨迹重复渲染不同背景，增加视觉多样性，不能计为等量的独立动作策略。

建议保留失败样本与恢复轨迹并标注用途；如果 imitation learning 只学习成功专家，要说明筛选规则，避免数据集只覆盖“容易成功”的初始状态。

### 10.4 规模化的实际瓶颈

除物理步数外，还需测 asset 加载、碰撞预处理、相机渲染、内存、图像编码、网络传输和写盘吞吐。平台声称的仿真 FPS 不应直接解释为带多相机/触觉的可用训练样本吞吐。

建议分别测“物理-only”“物理+策略传感器”“完整专家+渲染+写盘”三种配置，并公布场景大小、并行环境数、图像分辨率、接触复杂度和成功样本比例。

## 11. 如何评估模型的最终执行效果

### 11.1 必须分开的三种评估

| 评估 | 关注问题 | 合适的证据 |
|---|---|---|
| 资产/仿真器验证 | 同输入是否表现合理，与真实系统误差多大 | 尺寸、FK、响应、接触与传感标定 |
| 策略闭环评估 | 在固定任务分布中能否完成目标 | 逐 episode 日志、成功率、效率、失败类型 |
| 真机部署评估 | 能否长期、稳定地完成真实任务 | 未剪辑试验、重试/干预、运行时长与边界工况 |

模型预测损失、离线动作误差和演示视频有帮助，但不能替代真正推进环境后的闭环任务执行。

### 11.2 三家公开结果的可比性

| 对象 | 可确认的评估口径 | 不能直接横向比较的原因 |
|---|---|---|
| GraspVLA 论文抓取 | 最多 3 次尝试；目标抬升至少 15 cm；另报告效率指标 | 其 LIBERO 评测选择并改写抓取任务，不等于完整原始任务套件 |
| Sudo R1 发布介绍 | 首次/两次内成功率和连续运行演示 | 对象、布局、次数、人工处理与统计样本需对应完整日志 |
| Genesis AI 公司展示 | 公司披露任务展示与能力 | 本次未取得可与前两者统一重跑的完整评估协议 |

第一行依据[论文附录 E/G][s01]，第二行依据[官方 R1 页面][s02]。这些数字不能据此给出公司能力排名。

GraspVLA playground 提供按任务/种子运行、加载初始状态、调用远程策略和保存视频的评估代码，可用于学习协议实现，但本次没有运行。[锁定版本 evaluate_libero_tasks.py][s37]

### 11.3 建议的核心指标

| 维度 | 指标 | 为什么需要 |
|---|---|---|
| 完成质量 | 首次成功率、允许 K 次内成功率、任务级成功率 | 避免重试掩盖首抓不足 |
| 时间效率 | 单任务耗时、首次成功耗时、持续吞吐、有效运行比例 | 区分高成功率与生产效率 |
| 动作效率 | TCP 路径、动作数、停顿、重规划/反复开合 | 识别犹豫与冗余行为 |
| 约束 | 碰撞、掉落、越限、超力、物体损坏 | 成功不能忽略代价 |
| 恢复 | 扰动后恢复率、恢复时间、人工干预 | 反映真正闭环能力 |
| 泛化 | 未见实例/类别、布局、光照、相机、物性、本体 | 明确模型在哪些分布可用 |
| 系统一致性 | 延迟、抖动、丢帧、时间错位、跟踪误差 | 区分模型与接口/系统故障 |

抓取成功应写成可执行条件。例如“指定物体离开支撑面达到阈值、保持规定时长、夹爪没有非物理附着、没有禁用碰撞”。阈值由目标任务设定；不能把任一论文的 15 cm 直接规定成所有 Xense 任务标准。

插接需测最终插入深度、姿态误差和峰值力；放置需测稳定后的目标位置/朝向；长程任务还需子任务完成顺序、整体成功率和中途干预。

### 11.4 统计报告与失败分析

建议公布成功次数/总次数、随机种子、物体清单、任务分布及置信区间；多次运行同一物体、相邻时刻样本不应当作完全独立试验。

例如 100 次独立试验全部成功，并不能证明失败率为零；常用近似“rule of three”给出 95% 单侧失败率上界约 3%。这是统计解释示例，不是三家公司实验结果。

失败标签至少区分：感知目标错误、可达性/规划、TCP/坐标、控制跟踪、夹爪几何/耦合、接触物性、同步、策略决策和成功判据错误。先确定故障属于哪层，再决定修模型、修仿真参数还是补数据。

### 11.5 建议的统一评测矩阵

| 轴 | 基础组 | 泛化/压力组 |
|---|---|---|
| 对象 | 已见类别的新实例 | 未见类别、透明/反光、细长/易变形 |
| 场景 | 稀疏平面 | 杂乱、遮挡、靠边、狭窄通道 |
| 相机 | 标定名义配置 | 安装微扰、光照、背景、曝光与延迟 |
| 操作 | 普通抓取与放置 | 指定抓取区域、精确放置、插接、扰动恢复 |
| 物性 | 名义参数 | 有依据的摩擦/质量/柔顺性变化 |
| 本体 | 同一型号/工具 | 换夹爪、转接件或机械臂后单独评估 |

先固定基础组和实际输入/动作协议，再扩展测试分布。跨引擎复现可以发现数值敏感性，但也不能替代真机试验。

## 12. IK / FK 与 TCP / 关节控制

### 12.1 FK：输入关节状态，输出指定 frame 的位姿

对串联链，FK 将各关节的固定安装变换和运动变换相乘；末端再乘工具变换：

```text
T_base_tcp(q) = [∏ᵢ (T_parent_joint_i · T_motion_i(q_i))] · T_flange_tcp
```

几何 mesh 不决定 FK；关键在 joint origin、axis、类型、零位和 TCP 安装。base→flange 的 FK 正确，也不能证明法兰后接的相机和工具变换正确。

建议每个型号保存可追溯的“关节配置 → TCP 参考位姿”样本，与厂商控制器或实测比较；包括零位、工作区内部、多姿态及靠近限位的样本。闭链/欠驱动工具需要同时验证约束与从动关系。

### 12.2 IK：给目标 pose，求满足约束的 q

IK 除位置/姿态误差，还要处理限位、初值、解分支、冗余、奇异和碰撞。得到一个可达目标，不保证存在可安全执行的连续路径。

常见数值方法使用雅可比与阻尼最小二乘；以下仅是说明关系的局部更新式：

```text
Δq = Jᵀ (J Jᵀ + λ² I)⁻¹ e
q_next = q + Δq
```

`e` 的平移与旋转需统一 frame 并设置权重；实际求解还需要步长/限位约束和收敛判断。末端姿态误差不能不加说明地用欧拉角逐项相减。

多解情况下可利用上一帧 q、距离权重或零空间目标保持姿态连续；双臂还需避免分别求 IK 后出现臂间碰撞。

### 12.3 三条路线中的具体证据

| 对象 | 能确认的实现 | 仍不能确认的内容 |
|---|---|---|
| GraspVLA 规划端 | playground 用 URDF、`ee_link`、明确 joint list 与 cuRobo 配置 | 内部所有生产任务的求解设置 |
| GraspVLA 真机端 | 客户端接收末端增量，发布笛卡尔阻抗目标 | 不能概括其全部机器人都用同一控制器 |
| Sudo R1 | 官方描述逐步观察闭环 | TCP/关节动作表示、IK 算法、servo 增益与频率 |
| Genesis World | 提供 IK、multi-link/batched IK、规划与关节控制 | 不能直接推出 Genesis 公司策略头和本体伺服设计 |

cuRobo 的公开 v1 文档列出 FK/IK、碰撞检查与轨迹生成能力；当前主仓库已提示 V2 API 改变，重现历史环境应锁版本，不能把新接口直接用于旧代码。[cuRobo v0.7.8][s38]、[当前官方仓库][s39]

Genesis 的教程将 IK 解交给路径规划，再通过 `control_dofs_position()` 和 `scene.step()` 执行；多 link / 并行 IK 另有接口。直接 `set_dofs_position()` 展示姿态属于状态设置，不能替代有动力学的执行评估。[Genesis IK 与规划][s40]、[高级/并行 IK][s41]

ManiSkill 允许选择关节 PD 或末端 pose 控制；末端动作可通过 IK 转为关节位置目标。它还区分 world、root、body 等动作 frame。[ManiSkill 控制器][s42]

### 12.4 GraspVLA 真机客户端的动作与 TCP 变换

本次读取的 `grasp_mode.py` 将模型输出解释为 **3 维平移增量 + 3 维旋转增量 + 1 维夹爪动作**；代码累积平移并以左乘方式更新旋转矩阵。因此这一实现的旋转增量不能随意改成右乘的工具系增量。[锁定版本 grasp_mode.py][s27]

`franka_ros_controller.py` 使用 `panda_link0` 与 `panda_EE`，发布 `/cartesian_impedance_controller/equilibrium_pose`；启用扩展手指时，在真实 EEF 与策略 EEF 之间设置 0.03 m 的局部 Z 偏移，并在发送目标前进行逆变换。[锁定版本控制器][s43]

**工程判断：** 这是明确的跨接口 frame 适配证据。该偏移不是所有夹爪通用的“手指延长量”，也不是可直接套给 TacCap 的 TCP。需要按实际工具安装和控制点重新核对。

### 12.5 TCP 与关节控制为什么可以同时存在

```text
图像/触觉/本体状态
  → 策略：TCP pose、Δpose、joint target 或其他动作表示
  → 动作适配：frame 变换、单位、反归一化、限幅、时间调度
  → 运动生成：IK/微分 IK/规划，或笛卡尔阻抗雅可比映射
  → 关节执行：位置/速度/力矩目标及执行器动态
  → 实际运动与接触
  → 下一次观测
```

笛卡尔阻抗可通过 `Jᵀ` 将末端误差产生的 wrench 映射为关节力矩，并加入零空间、动力学补偿和约束处理；它不一定每一步先求一个完整 IK 角度解。因此“TCP 控制 = 必然先完整求 IK”也过于简单。

| 策略动作 | 适用特点 | 必须说明 |
|---|---|---|
| 绝对 TCP pose | 目标易解释 | 世界/base/tool frame、TCP、姿态表示 |
| TCP Δpose / velocity | 适合闭环局部修正 | 增量 frame、旋转乘法方向、dt、尺度 |
| joint position / Δq | 便于按本体执行 | joint 顺序、rad/m、限位和耦合 |
| joint velocity | 速度反馈 | 积分、饱和和采样周期 |
| joint torque / effort | 直接研究动力学与接触 | 惯性/执行器精度、补偿和力矩定义 |
| gripper width / command | 夹爪独立控制 | 总开口还是单指位移、力限制、连续/离散 |

建议为每个策略 checkpoint 保存动作 schema，防止模型输出与执行接口悄悄变化。原始动作、限幅后的命令和实际测量值都应写入日志。

### 12.6 控制频率与闭环定义

至少分别报告：物理积分、关节伺服、传感器采样、策略推理和动作更新时间。15–25 Hz 的视觉策略不意味着电机伺服或接触求解也是该频率。

动作块策略可在高频执行低频推理产生的多步动作；要说明一次执行多少步、是否接受新观测、如何抢占。逐步观察策略也要核对拿到的是新帧还是缓存旧帧，不能只以循环次数证明视觉闭环频率。

## 13. 面向 Xense 资产与仿真团队的落地建议

### 13.1 当前资产仓库优先完成的工作

已阅读本仓库 `AGENTS.md`、`docs/ASSET_STANDARD.md` 与 `docs/ASSET_INVENTORY.md`。下列建议与当前范围一致；**本次没有修改仓库资产或新增仿真调用代码。**

| 优先级 | 工作 | 交付与验收 |
|---|---|---|
| P0 | 来源、型号、左右和单位 | 原件快照、许可证、SHA-256、逐字段待核对状态 |
| P0 | 结构、零位、axis、限位和耦合 | viewer 正向扫描、左右一致性、硬件依据 |
| P0 | flange/TCP/相机/触觉 frame | 显式安装变换及标定来源，未知项不估算 |
| P0 | 资源可搬移 | 相对路径、mesh/MTL/纹理完整、ZIP 搬移检查 |
| P1 | visual/collision 派生记录 | 不覆盖原 mesh；记录工具、参数和用途 |
| P1 | 消费端名称/动作顺序映射 | 运行时枚举与静态配置比对 |
| P1 | 惯性与接触核对 | 先确认来源，再做 CAD/测量/辨识，不靠外观补猜 |
| P2 | 按需求派生 USD/MJCF | 单独说明解析、运动学、动力学和接触验证范围 |

装配只引用资产并描述连接；控制器、环境、数采和 RL 留在各自仓库。`python/` 不作为打包运行时接口。

### 13.2 建议安排的最小验证闭环

1. 从清单中选定**已接入且来源可追溯**的一台机械臂、一套 TacCap 从夹爪及真实转接件配置。
2. 核对实际安装、TCP 与相机/触觉 frame；先验收 viewer 和 FK，不将其称为动力学通过。
3. 在独立消费项目中选一个仿真后端，检查导入后的关节、惯性、碰撞与动作映射。
4. 用少量固定物体做“接近—闭合—抬升—放置”，逐帧记录命令、实际状态、图像与接触。
5. 对失败分类，明确是资产/标定、控制、接触还是策略，再决定扩大数据规模。
6. 基础闭环通过后才做跨格式、跨引擎与更广分布评测。

这里没有指定具体机器人型号已通过完整仿真。资产目录的“已接入”只说明登记状态，不能代替各项实物验收。

### 13.3 厂商对接应索取的证据

| 主题 | 建议索取 |
|---|---|
| 模型精度 | 型号/硬件 revision、原始 CAD/描述、mass/COM/inertia 来源和误差 |
| 坐标 | 基座/法兰/TCP/相机/触觉 frame 定义，手眼/双目标定及时间基准 |
| mesh | 原件与派生、尺度、visual/collision 区分、面数、几何偏差、凸分解参数 |
| 格式 | 权威来源、导出工具/版本、丢失字段、固定件合并、名称映射 |
| 控制 | action schema、joint 顺序、IK/阻抗路径、增益/饱和/延迟与夹爪耦合 |
| 传感 | 取图/触觉接口、shape/dtype/unit/frame、采样与延迟、噪声模型 |
| 数据 | 数据分布、有效 episode、成功筛选、真实/合成占比、划分与许可证 |
| 评估 | 对象与场景列表、尝试次数、success 判据、完整日志、人工干预和置信区间 |

供应商若只能提供渲染图，应记录为外观证据；若只能提供 URDF，记录为结构/字段证据；只有接触与实机实验才能进一步支持对应任务的物理准确性。

## 14. 来源索引、抽查复现与未覆盖项

### 14.1 核心来源索引

下列均优先采用论文、作者仓库、公司直接发布材料或平台官方文档。正文链接使用同一索引，可在线查看。动态文档需按实际项目锁定版本。

| 编号 | 来源 | 主要用途 |
|---|---|---|
| S01 | [GraspVLA 论文 v2][s01] | 数据生产、实验口径与适配边界 |
| S02–03 | [Sudo R1][s02]、[官方招聘][s03] | 公司声明与 ManiSkill 等研发线索 |
| S04 | [Genesis AI 发布的 GENE-26.5 新闻稿][s04] | 公司数据与硬件路线；非第三方评测 |
| S05、S07 | [Genesis World][s05]、[发布记录][s07] | 开源平台与版本 |
| S06、S10、S16 | [示例 URDF][s06]、[规划配置][s10]、[mesh][s16] | 本次文件级抽查 |
| S08–09 | [playground][s08]、[真机客户端][s09] | 运行与评估入口 |
| S11、S13、S15、S17、S22 | [Nyx][s11]、[坐标][s13]、[索引][s15]、[mesh 处理][s17]、[资产加载][s22] | Genesis 资产与渲染基础设施 |
| S12、S20 | [REP-103][s12]、[UsdPhysics][s20] | 坐标约定与物理 schema |
| S14、S28–29、S34 | [Isaac 导入器][s14]、[相机][s28]、[迁移][s29]、[触觉资产][s34] | 平台当前能力与版本变化 |
| S18–19、S21 | [MuJoCo mesh][s18]、[modeling][s19]、[OpenUSD][s21] | 格式语义与碰撞边界 |
| S23、S30、S36、S42 | [ManiSkill GPU][s23]、[相机][s30]、[记录][s36]、[控制器][s42] | 公开生态机制，不证明 R1 部署实现 |
| S24 | [Objaverse][s24] | 物体几何来源参考 |
| S25、S31–32、S35 | [Genesis 相机][s25]、[接触力][s31]、[触觉][s32]、[记录][s35] | 仿真数据接口 |
| S26–27、S43 | [相机包装][s26]、[策略客户端][s27]、[控制器][s43] | 源码级图像/动作/TCP 检查 |
| S33 | [TACTO][s33] | 视触觉渲染与物理精度边界 |
| S37–41 | [评估代码][s37]、[cuRobo v1][s38]、[cuRobo 当前][s39]、[Genesis IK][s40]、[高级 IK][s41] | 执行与运动学机制 |

GraspVLA 当前主仓库还提供训练与数据链接，并列出 2026-08-19 数据发布更新；不应继续按早期论文的未来时态写成“尚未发布”。具体数据字段、访问与授权应以[主仓库][s44]和[SynGrasp-1B 数据页][s45]为准，论文、代码和数据的许可证分别核对。

### 14.2 文件抽查的复现依据

公开源仓库：`MiYanDoris/GraspVLA-playground`，提交 `4d3d4b5b4568dbaf27f71390fd71ef170d800f70`。

```text
被检查 URDF：
assets/franka_with_extended_finger/franka_with_extended_finger.urdf
SHA-256：
59251c4c8f60e5ab0b72fb8868aa3df1af2707e5270c3d2c55ab3f383035d8c8

被检查规划配置：
assets/franka_with_extended_finger/franka.yml
SHA-256：
7e9a9f8ae862e9ebc6e38c3f32ef401b98c143c0f1da01f9075ad3db904a4a77

真机客户端仓库：MiYanDoris/GraspVLA-real-world-controller
提交：14e32ebd645e6f9a13da39f22dd1c8985fd4c8f9
vla_client/controllers/franka_ros_controller.py SHA-256：
742016b364695d3dc3b35a74cc02618a8c9ecfdc5f28bb07b5be632310a67d9b
```

二进制 STL 面数检查的核心关系为：

```text
N = little_endian_uint32(file_bytes[80:84])
确认 file_size == 84 + 50 × N
逐面读取三个顶点，统计各轴 min/max
```

该方法只用于已确认的二进制 STL；ASCII STL 不能直接套用。面数与包围盒用于发现复杂度/尺度异常，不提供 CAD 偏差、水密性或物性证明。

### 14.3 资料与验证限制

- 本次未取得三家内部生产资产、全套相机/触觉标定、完整控制器参数和同条件实机日志。
- Sudo 的 R1 详细底层架构、命名规范、网格和 IK/FK 实现仍待厂商提供材料。
- Genesis 公司原博客/新闻 URL 在本次直接访问时返回站点通用页面；公司数据路线改用其发布在 PR Newswire 的原始新闻稿，平台能力以官方仓库与文档为准。
- 某些 ROS 官网页面触发访问保护；REP-103 采用 ROS 官方维护仓库中的原文。
- 公开示例文件的简化数值与路径问题，不可推广成内部生产系统存在同样问题。
- 本次没有执行 URDF/MJCF/USD 仿真、渲染、ROS 安装、ZIP 资产搬移或机器人真机实验；未对动力学、摩擦、接触、传感标定和长期可靠性作通过结论。

[s01]: https://arxiv.org/html/2505.03233v2
[s02]: https://www.sudo.ai/
[s03]: https://www.sudo.ai/zh/careers/
[s04]: https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html
[s05]: https://github.com/Genesis-Embodied-AI/genesis-world
[s06]: https://github.com/MiYanDoris/GraspVLA-playground/blob/4d3d4b5b4568dbaf27f71390fd71ef170d800f70/assets/franka_with_extended_finger/franka_with_extended_finger.urdf
[s07]: https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.4
[s08]: https://github.com/MiYanDoris/GraspVLA-playground
[s09]: https://github.com/MiYanDoris/GraspVLA-real-world-controller
[s10]: https://github.com/MiYanDoris/GraspVLA-playground/blob/4d3d4b5b4568dbaf27f71390fd71ef170d800f70/assets/franka_with_extended_finger/franka.yml
[s11]: https://genesis-embodied-ai.github.io/genesis-nyx/
[s12]: https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-0103.rst
[s13]: https://genesis-world.readthedocs.io/en/latest/user_guide/configuration/conventions.html
[s14]: https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/ext_isaacsim_asset_importer_urdf.html
[s15]: https://genesis-world.readthedocs.io/en/latest/user_guide/developers/naming_and_variables.html
[s16]: https://github.com/MiYanDoris/GraspVLA-playground/tree/4d3d4b5b4568dbaf27f71390fd71ef170d800f70/assets/franka_with_extended_finger/meshes
[s17]: https://genesis-world.readthedocs.io/en/v1.4.0/user_guide/assets/mesh_processing.html
[s18]: https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh
[s19]: https://mujoco.readthedocs.io/en/stable/modeling.html
[s20]: https://openusd.org/release/api/usd_physics_page_front.html
[s21]: https://mujoco.readthedocs.io/en/stable/OpenUSD/index.html
[s22]: https://genesis-world.readthedocs.io/en/v1.2.2/user_guide/assets/loading_assets.html
[s23]: https://maniskill.readthedocs.io/en/latest/user_guide/concepts/gpu_simulation.html
[s24]: https://objaverse.allenai.org/
[s25]: https://genesis-world.readthedocs.io/en/latest/user_guide/sensing/camera_sensors.html
[s26]: https://github.com/MiYanDoris/GraspVLA-real-world-controller/blob/14e32ebd645e6f9a13da39f22dd1c8985fd4c8f9/vla_client/utils/cameras.py
[s27]: https://github.com/MiYanDoris/GraspVLA-real-world-controller/blob/14e32ebd645e6f9a13da39f22dd1c8985fd4c8f9/vla_client/modes/grasp_mode.py
[s28]: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera.html
[s29]: https://docs.isaacsim.omniverse.nvidia.com/latest/migration_guides/isaac_sim_6_0/sensors_camera_to_experimental_rtx.html
[s30]: https://maniskill.readthedocs.io/en/latest/user_guide/concepts/sensors.html
[s31]: https://genesis-world.readthedocs.io/en/latest/user_guide/sensing/contact.html
[s32]: https://genesis-world.readthedocs.io/en/latest/user_guide/sensing/tactile.html
[s33]: https://github.com/facebookresearch/tacto
[s34]: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_tactile_sensors.html
[s35]: https://genesis-world.readthedocs.io/en/latest/user_guide/sensing/recorders.html
[s36]: https://maniskill.readthedocs.io/en/latest/user_guide/wrappers/record.html
[s37]: https://github.com/MiYanDoris/GraspVLA-playground/blob/4d3d4b5b4568dbaf27f71390fd71ef170d800f70/evaluate_libero_tasks.py
[s38]: https://github.com/NVlabs/curobo/tree/v0.7.8
[s39]: https://github.com/NVlabs/curobo
[s40]: https://genesis-world.readthedocs.io/en/latest/user_guide/robot_control/inverse_kinematics_motion_planning.html
[s41]: https://genesis-world.readthedocs.io/en/v1.2.2/user_guide/robot_control/advanced_ik.html
[s42]: https://maniskill.readthedocs.io/en/latest/user_guide/concepts/controllers.html
[s43]: https://github.com/MiYanDoris/GraspVLA-real-world-controller/blob/14e32ebd645e6f9a13da39f22dd1c8985fd4c8f9/vla_client/controllers/franka_ros_controller.py
[s44]: https://github.com/PKU-EPIC/GraspVLA
[s45]: https://huggingface.co/datasets/vegebirrd/SynGrasp-1B
