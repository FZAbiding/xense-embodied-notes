> 历史文档快照：原记录日期 2026-10-15，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](../sources.md)。

> 以下调研保留原记录时点的输入与结果；本轮归档与核对来源引用，当前交付和新旧碰撞边界以各资产usd/source.json及本轮验收记录为准。

# 现有 USD 来源审查、下游风险与下一阶段规划（2026-10-15）

现有 USD 有可追溯来源，但**官方来源不等于可直接用于动力学或抓取**。
本次发现 FR3 惯量差异、历史 Rizon4R 碰撞解析及材质问题；夹爪版本、固定根、耦合后端和分发范围也需要明确。
下一阶段先修复/验收现有资产，再补工具与静态环境，形成一个可运行的最小工位。
本轮没有新增转换资产，也没有改写厂家 USD 原件。

## 审查范围与证据

本次工作区实际有 **9 个资产包含 USD、13 个入口、74 个 USD 层文件**；
遍历了 22 个根变体组合。目录检查为 33 资产 / 24 装配 / 1,409 个登记文件。
这是未提交工作区的文件快照，不能把 HEAD 当作所有实际输入的版本；文件哈希已随报告锁定，
结束时 104 个审查锁定文件仍一致。并行迁移的新 TacCap 不与旧版混算。
完整机器可读证据见 [审查 JSON（工作区资料，未随文保存）](../sources.md#workspace-2e928425b247)。

实际执行了官方 Git tree/发布包来源核对、OpenUSD 26.08 的 28 个已注册验证器、
物理描述解析、依赖搬移、CS66/ACOne 数值复查及主从爪定向测试。
没有运行 Isaac/PhysX/Newton、目标材质渲染或硬件标定；没有在本轮重新安装迁移后的 wheel 或执行 ROS share 安装。

## 哪些是官方 USD

| 资产 | 当前 USD 来源结论 | 本次依据 |
|---|---|---|
| Flexiv Rizon4 | 厂家原件快照 | `isaac_sim_ws@b28e3bd0…` v2.2.0；本地字节哈希、Git blob 与远端固定 tree 一致 |
| Flexiv Rizon4S | 厂家原件快照 | 同一官方提交；独立于 URDF 来源，保留腕部 FT 拆分 |
| Flexiv Rizon4R | 历史厂家原件快照 | `isaac_sim_ws@7740596c…`；远端 blob 一致，不冒称当前 v2.2.0 |
| Seeed B601-RS | 厂家原件快照 | `reBot-Isaacsim@158f8731…`；远端 blob 一致，含原厂夹爪 |
| Franka FR3 v2.1 | 厂家发布包原件 | `franka_simulation` v0.1.0；重新下载 5,560,164 字节归档，SHA-256 与厂家清单一致，11 个归档文件逐字节一致 |
| Elite CS66 | 本地 URDF 派生，不是厂家发布的 USD | `urdf-usd-converter==0.3.3`；实际输入锁一致，24 个厂家输入 blob 与固定 tree 一致 |
| ARX ACOne | 本地 URDF 派生，不是厂家发布的 USD | 同一转换器；重新下载官方 7z，核对归档哈希及 17 STL + 原始 URDF 共 18 个文件；转换输入锁一致 |
| TacCap 主爪 `xense.taccap_master` | 公司官方公开发布的原件，能力为显示/动画 | 公司 `XTac-UMI-Description@c46c088…`；14 个 USD 文件与公开源字节及远端 blob 一致 |
| TacCap 旧从爪 `xense.taccap_slave` | 公司官方基线上的本地派生，不是未改动的发布原件 | 当前位于 `slave-v2026.08.03`；8 个 USD 文件是已记录的修订，本地哈希吻合；8 个原始发布文件的源哈希另从远端复核 |

完整提交、厂家 URL 和逐文件结果见 JSON 及各机器人 `usd/source.json`。
公司主从爪使用 `assets/grippers/xense/taccap/upstream.json` 记录公开源与本地派生的差别。
**新版 `xense.taccap_slave_v2026_10_15` 当前没有 USD**，只有两套 URDF 入口；不能将旧版 USD 宣称为新版资产。

来源官方与分发授权分别记录：Franka 独立 USD 发布物和 ARX 的许可仍未确认；
本轮不推断额外授权。现有公开浏览器白名单仅列公司主从爪，不因本次核查自动扩大发布范围。

## 已复现的问题和潜在下游错误

### 1. FR3 的完整惯量不等价：优先处理

当前标准规则检查没有诊断，但重新从主轴与对角惯量重建完整张量后，
与同型号官方 URDF 的最大元素差仍为 **0.01311105846 kg·m²**；
主轴取共轭后差异降至 float 精度附近。此结果与历史比对一致，不能当作材质环境问题。
上游转换器更新日志记录过相关方向修复，是原因线索；本轮没有运行求解器确认动态后果。

下游风险是质量看起来正确、场景也能打开，但角加速度和控制响应可能与源模型不一致。
保留厂家原件；候选修正须另存有来源的覆盖层，或等待厂家新包，再进行完整张量与目标后端回归。
不能用改驱动增益掩盖该差异。见 [原比对（工作区资料，未随文保存）](../sources.md#workspace-a4f6f1b2e0ef)和本次 JSON 的 `detail_rechecks`。

### 2. Rizon4R 的碰撞与材质：不宜直接作为接触任务基线

这是旧结构 USD，本轮发现：

- OpenUSD 26.08 标准物理解析器报告 9 刚体、7 转动 + 2 固定关节，**未收集到碰撞形状描述**。
  8 个 CollisionAPI 位于 `collisions` 容器，解析器逐项警告 unknown UsdGeomGPrim type。
  这说明使用该解析路径的消费链存在丢碰撞风险；未执行 PhysX，不能据此断言所有引擎都会相同。
- 28 项验证器共报告 **14 条 Error 诊断**：6 条 materialBind 子集 family type 错误，
  7 条 MDL sourceType 未注册，以及 1 条 `OmniPBR.mdl` 无法解析。
- 6 条子集错误属于现有数据规则问题，不能全部归结为检查环境缺材质插件。

目标环境须实测有效碰撞形状数量及接触，材质子集也要独立修复/验收。
修正层应保留原几何和变换；不能悄悄把原件改成另一套模型、替换为 Rizon4M 或以密度补猜物性。

### 3. TacCap：显示资产、动力学资产与版本不能混用

主爪左右及开合动画共 4 个入口，标准解析为 **0 刚体、0 物理关节**，属于显示/动画资产。
下游不能据此创建物理 articulation 或读取关节力矩。

旧从爪 bare/with_mount 两个入口有刚体、源碰撞凸包、驱动及 `PhysxMimicJointAPI`，
都含连接世界的 `root_fixed_joint`。作为独立固定爪使用是既有配置；挂到活动机械臂时，
消费端需要处理世界锚定、 articulation 边界和附着约束，否则可能固定工具到世界或形成过约束。
PhysX mimic 字段的存在不能证明 Newton 或其他消费者已执行同一耦合；需明确适配并验收开合。

旧版 bare 总质量为 0.750 kg，mounted 为 0.770 kg，但内部质量分配采用不同修订，
COM/惯量仍是带警告的来源/临时值；不能当作经过一致辨识的“仅增加一个转接件”。
本轮主从 USD 的 **30 项定向测试通过**，覆盖数据与既有约定，不是新的动力学或接触验收。

兼容 API `get_usd_path()` 有意指向 `slave-v2026.08.03/usd`，不是新版六部件从爪。
旧路径 `slave/usd` 当前不存在；硬编码旧路径的下游会失败。
迁移后的源码 API 路径已实测存在，安装后的旧/新包不能仅凭同一个函数名判断模型版本。

### 4. 通用 ZIP 分发范围：实测没有 TacCap USD

现有公司主/旧从 USD 共 **22 个文件没有登记到各自 asset.json.files**，由公开源锁另行管理。
使用 `export_urdf_bundle.py --asset xense.taccap_master --asset xense.taccap_slave` 的实际 ZIP
有 85 个成员，**USD 文件数为 0**。这是当前 URDF 导出器的能力边界，不是 USD 文件损坏。
但如果把这个 ZIP 当作全格式资产包，下游会缺模型。

下一阶段应统一来源清单和可选格式导出契约，或提供明确的 USD 包；不应默认依赖 wheel 的 glob
恰好包含文件。TacCap 迁移后还应做一次干净 wheel 构建、安装搬移和 ROS share 检查。
本轮此前 CS66/ACOne 的 wheel 验证不能替代新版 TacCap 迁移后的安装验收。

### 5. 官方验证器误扫派生资产：本轮已修复

原 `validate_official_usd.py` 默认扫描全部 `usd/source.json`，遇到 CS66/ACOne 的派生清单
会因为不存在厂家原字节字段而抛出 `KeyError: source_sha256`，已实际复现。
现已按 `kind == official_snapshot` 筛选；显式对派生资产使用该检查器会提示应做来源等价检查。
新增来源路由回归与 FR3 官方来源回归共 **5 项通过**；实际默认命令完成 5 套厂家快照及 ZIP 搬移。

该工具仍将合规诊断与来源/搬移结论分开，命令退出 0 不表示材质合规。
CI/下游验收应检查报告字段和所需能力，不能只看退出码或 “zip_relocation passed”。

### 6. CS66 / ACOne：数据等价通过，接触与消费配置仍待验

两款以 0.3.3 转换的当前输入/输出哈希未漂移；重新执行 79 / 99 组姿态、完整惯量和全部三角形比对通过。
但当前碰撞为源三角网格 `approximation=none`，动态非凸接触支持须按目标后端另验；
层级刚体在不同消费实现中的支持也需核查。
[上游 README](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/README.md)
明确提示其他物理消费实现可能需要适配。

CS66 保留源固定根；ACOne 保留浮动根。直接把 ACOne 当作固定桌面机器人运行，会与消费预期不同。
本机 `xense-genie_sim` 的 `scene_flat_acone.yaml` 当前使用它自己的机器人生成链，**尚未直接加载本仓库 USD**。
若替换进去，该配置的六个初始关节名 `arm_l_joint* / arm_r_joint*` 在本 USD 中不存在，
`arm_l_end_link / arm_r_end_link` 两个相机父帧也不存在，必须显式做名称/帧/固定根适配。
这是替换时的已确认接口差异，不宣称该消费配置当前已经运行失败。

### 7. 其他组合风险

- Rizon4 / Rizon4S / FR3 默认 Physics=physx，Seeed 默认 Physics=physics；不能依赖统一默认后端。
  Rizon4 / Rizon4S / FR3 的 none 变体中仍有 8 个 CollisionAPI，不能把 none 自动理解为所有碰撞都已禁用。
- Rizon4/Rizon4R USD 与当前 URDF 的 link 名不同，Rizon4S 另有腕部 FT 拆分。
  URDF 装配连接帧不能不经映射直接用于 USD。
- Seeed 官方 USD 含完整原厂夹爪，当前 URDF 的裸臂、独立夹爪及用户派生 mimic 是不同配置。
  叠加独立夹爪前应检查原厂夹爪是否仍存在，避免重复工具和质量。
- 10.15 TacCap 的 C4 与旧独立 Asm_link 连接件不是同一个来源零件。
  新 with_mount 资产已含 C4，不能仅凭名称相似再添加旧连接件形成重复装配。
- 通用机器人 USD 目前从资产根下的 `usd/source.json` 读取入口；`asset.json.entrypoints` 仍是 URDF 契约，
  `get_usd_path()` 是旧 TacCap 兼容接口，不能拿它查询任意机器人。

## 本次合规复查如何更新旧结论

此前 25.11 环境的厂家着色器诊断仍保留为历史记录。
本次使用 `usd-exchange==3.0.1` 携带的 OpenUSD 26.08：
除 Rizon4R 外，其余 8 个 USD 资产的全部已检查根变体，在 28 个已注册验证器下没有诊断。
这说明此前多项 PreviewSurface 检查受环境/版本影响，不能继续把旧诊断当作当前唯一结论；
也不能把新规则通过当作真实材质渲染或动力学成功。FR3 正是规则通过而完整惯量比对有差异的例子。
Rizon4R 仍有实际子集问题和未满足的 MDL 依赖，需要分开处理。

## 下一阶段优先做哪些 USD

以下是制作与验收规划，本轮没有执行这些新转换。优先完成已有机械臂的可用工位，
不按厂商清单批量扩充裸臂文件。

| 顺序 | 对象 / 工作 | 为什么优先 | 完成门槛 |
|---|---|---|---|
| P0：现有资产修复与消费验收 | FR3 修正候选；Rizon4R 碰撞/材质候选；TacCap 来源/导出/版本契约 | 防止把已知问题带入新场景 | 原件保留；修正独立可追溯；指定后端有效碰撞、惯量与耦合检查；完整分发与安装搬移 |
| P1a：静态环境 | `worktable.120cm`、`elite_cs66.a1_stand`；随后 `diagonal_02.stand` | 给现有 CS66/Flexiv 提供实际工作空间，依赖和运动结构简单 | 几何/单位/安装变换/碰撞误差可追溯；无物性输入时只做静态或可视资产，不赋动态密度/质量 |
| P1b：新版从爪 | `xense.taccap_slave_v2026_10_15` 的 default / with_mount | 本项目核心工具，新版当前缺 USD，能复用已有 CAD/URDF | 先冻结六部件输入和公共 flange；相机 COM/指姿态问题有明确结论或限定交付边界；完整张量、mimic、根约束与目标后端开合/接触验收 |
| P1c：连接件 | Flexiv/Elite/Franka→TacCap 的旧 Asm_link；Seeed→TacCap C1 | 让已有臂与工具能通过引用组合，避免复制几何和物性 | 区分 C4 与 Asm/C1；保留来源和安装变换。Asm 的 COM/惯量未提供时先交付几何/参考层，不称为动态等价工具链 |
| P2：最小工位试点 | 先单 CS66 + 明确版本的工具 + 桌/底座，再做 Diagonal-07 双臂 USD 组合 | 验证真正的下游消费链，暴露附着、命名和碰撞问题 | 引用已验收部件；处理固定根/ articulation 边界、左右实例路径与 start_pose；多姿态、逐关节、双臂与接触通过 |
| P3：复用已有臂扩展工位 | Diagonal-08、Flexiv 01/02；其后 04/05、Seeed 单臂/ACOne 场景 | 复用现有 USD，不重复转换机械参数 | FT/法兰/工具版本映射正确；Rizon4R 问题解决后再用于 04/05；ACOne 显式固定根和名称适配 |
| P4：按真实消费需求增加新型号 | 独立 Seeed 夹爪、Robotiq 2F-85；其后 Panda/FER、Tron2、灵巧手 | 避免在当前工具链尚未验收时引入更多耦合和控制复杂度 | Seeed 用户派生 mimic 明确；Robotiq 5 个 mimic 逐项验收；Panda link4 惯量三角不等式疑点须先登记/确认；Tron2 及手模型按需求另立后端验收 |

P1a 与 P1b 可以独立准备。新版 TacCap 物性审查未完成时，静态环境仍可推进；
不得为赶进度猜测相机 COM 或惯量。若先做新版可视预览，应明确不含已验收动力学。
静态桌/底座不需要伪造质量；移动场景才另行补有依据的刚体物性。

工位 USD 只保存部件引用、连接、实例配置及有来源的初始姿态，不复制另一套可独立编辑的机械参数。
现有 07 配方目前引用旧从爪，升级到新六部件爪需显式新配置与验证，不能悄悄替换现有装配。
多格式目录与装配 schema 如需扩展，先明确 USD 补充入口契约，继续保持 URDF 接口兼容。

所有新 URDF 派生 USD 继续锁定 `urdf-usd-converter==0.3.3`，记录输入、依赖及后处理；
转换脚本维护在 description 仓库外。已有厂家 USD 优先保留原件；新增 CAD 几何链才评估 usd-brep，
不把 STL 逆向拟合或未经误差验收的 BREP 网格化当作精度升级。

## 资料与复核入口

厂家来源及精确提交见 [来源总说明（工作区资料，未随文保存）](../sources.md#workspace-404ddbc1d75b)，行业依据见
[路线评估](../report.md)，检查层次见
[分层清单（工作区资料，未随文保存）](../sources.md#workspace-158fd289bedd)。
[Franka 官方发布](https://github.com/frankarobotics/franka_simulation/releases/tag/v0.1.0)、
[PhysX articulation/mimic 说明](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/articulations.html)
与本次测量应分别使用，文档支持的能力不等于已在本机运行。
原始审查工具和日志位于 `workspace-temp/xense-usd-audit-20261015/`，不是资产运行依赖。
