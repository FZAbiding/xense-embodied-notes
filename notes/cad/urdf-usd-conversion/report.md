> 历史文档快照：原记录日期 2026-10-15，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](sources.md)。

> 以下调研保留原记录时点的输入与结果；本轮归档与核对来源引用，当前交付和新旧碰撞边界以各资产usd/source.json及本轮验收记录为准。

# URDF → USD 路线的可行性与行业背景（2026-10-15）

本项目采用 **`urdf-usd-converter==0.3.3`**，从锁定的厂家 URDF/mesh 生成可追溯的本地派生 USD，
再独立核对数值与资源。对 CS66 / ACOne 的资产转换和分发，这条路线已有本项目实测支持；
对目标引擎中的动力学、驱动与接触，目前仍是待验收候选。不能把两种可行性合并评价。

厂家现成 USD 与本地转换的具体分类见 [来源总说明（工作区资料，未随文保存）](sources.md#workspace-404ddbc1d75b)；
版本锁、后处理及 usd-brep 实测见 [实施记录（工作区资料，未随文保存）](sources.md#workspace-158fd289bedd)。
本文补充背景资料，没有升级工具、重新转换资产或扩大既有验证结论。
现有全部 USD 的实际来源复查、Rizon4R 新发现及下一阶段交付顺序见
[全库审查与规划](topics/usd-source-audit.md)。

## 行业实践提供了什么依据

| 公开依据 | 可支持的判断 | 不能据此推出的结论 |
|---|---|---|
| [Isaac Sim 官方 URDF 导入教程](https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/import_urdf.html)给出 URDF→USD 输出、基座、碰撞及驱动配置流程 | URDF→USD 是该平台明确支持的资产接入方式 | 任意转换器、版本和默认参数都等价，或无需调整就可运行 |
| [Isaac Lab converter API](https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.sim.converters.html)提供 UrdfConverter | 机器人学习工具链也使用这一格式转换流程 | Isaac Lab 所用实现与本次独立 CLI 必然相同，或已验证本次输出 |
| [NVIDIA Omniverse 工具目录](https://developer.nvidia.com/omniverse)列出 urdf-usd-converter，定位为 USD 审查和面向 Newton 的工作流 | 本次工具有公开生态入口，选择有维护与集成依据 | 这是跨引擎通用认证或独立第三方推荐 |
| [Franka 官方模型与仿真页](https://franka.de/models-and-simulation)提供模型/仿真资源入口；本仓库已锁定 FR3 USD 发布包 | 厂家交付 USD 有实际案例 | 厂家发布物必然与 URDF 物理等价；本次 FR3 主轴差异已另行记录 |

上述证据主要来自平台维护者及厂家，是**行业使用依据与产品定位**，不是独立测评或行业一致意见。
本次检索没有获得针对 `0.3.3`、覆盖完整动力学/接触且可复核的独立横向评测，
因此不写“行业公认最优”“生产级通用转换”或无条件可靠的评价。

### 厂家工程记录：Seeed 的跨后端排查

[Seeed 官方仓库工程记录](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/158f87317fcaa35a7d1706ef364e324d3565939e/usd/RS-rebot-dev-arm/docs/VALIDATION_SKILL.md)
描述了使用同一转换器项目从 URDF 重建 DevArm 资产，并对 Newton/PhysX、碰撞开关及逐关节运动做对照。
它报告单凸包填平凹槽/夹爪间隙会阻挡运动，并区分静态稳定与动态跟踪。
这是厂家的单项目经验报告，本次没有重现其运行，也不是 `0.3.3` 对所有机器人的验证。

据此，本项目选择把驱动与接触配置留在消费端、记录碰撞近似并安排逐关节动态验收。
CS66/ACOne 的多关节限位姿态检查属于不执行碰撞的约束运动学比较；
未来带接触的引擎测试不能直接照搬“所有关节同时到上下限”的测试序列。
两个后端结果一致只是软件一致性证据，仍不能证明共同使用的物性或控制参数与实机一致。

## 工具成熟度与公开基准

[转换器固定提交 README](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/README.md)
仍将项目标为 **Alpha**，提供独立 CLI/Python 和分层、自包含资产输出。
这使离线构建易于隔离和追溯，但不能视为稳定性承诺；上游还明确提示其他求解器可能需要适配层级刚体。
[PyPI 0.3.3 发布页](https://pypi.org/project/urdf-usd-converter/0.3.3/)
对应 2026-08-07 的分发物。本项目以实际 wheel 哈希和完整依赖锁识别环境，不使用“latest”代替版本。

[上游 benchmark](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/benchmarks.md)
的报告时间为 **2026-04-17**，记录 408 个模型、394 个转换成功（96.6%）、14 个失败；
所列运行日志的工具版本为 **0.1.1**。这是维护者自报的历史批量转换结果，
其成功状态不能当作 `0.3.3` 的通过率、完整惯量精度、运行性能或接触准确率。
报告另列人工核验状态，不能把进程成功替换成已经人工/物理验收。

采用 0.3.3 的具体依据是
[更新日志中的修复](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/CHANGELOG.md)：
0.3.0 修正非对角惯量主轴方向，0.3.2 修正惯性 rpy，0.3.3 继续修正主轴来源及 ghost 帧处理。
它们直接关联本项目需要保留的完整惯量和参考帧，所以没有照用 FR3 厂家包标注的旧 0.1.2。
这些修复也是工具仍需版本锁和独立回归的证据，不能仅因为版本更高就认定所有问题已消失。

## 本项目的可行性判断

以下是基于输入条件与本次测试的工程判断，不是上游承诺。

| 维度 | 当前判断 | 依据与边界 |
|---|---|---|
| 输入适配 | CS66 / ACOne 可行 | 都有锁定 URDF、逐 link 网格及来源物性，无须从 CAD 猜轴向、限位或惯量 |
| 离线与可重复构建 | 可行 | CLI、完整依赖锁、分发包哈希、输入/输出哈希和后处理记录已保存；脚本在仓库外 |
| 运动学/惯量/几何映射 | 已通过这两款的限定检查 | 79 / 99 组姿态、完整张量、全部三角形及缺陷负对照通过；不代表所有 URDF 特征均已覆盖 |
| USD 结构与分发 | 已通过限定检查 | OpenUSD 26.08 验证器、ZIP 搬移、wheel 安装搬移与 25.11 读取通过 |
| 目标后端运行 | 待验收 | 尚未启动 Isaac/PhysX/Newton；需要核查层级刚体、锚定、schema 和约束消费方式 |
| 动态碰撞与抓取 | 待验收 | 源三角表面保留为 approximation=none；没有把未验证的单凸包当作等价碰撞 |
| 实机准确性 | 待核对 | 输入原值不等于辨识精度；CS66 厂家警告与 ACOne 未确认项继续保留 |
| 扩展到其他型号 | 逐项评估 | 不能从两款成功外推到闭链、mimic、缺惯性、特殊 mesh 或厂商扩展 |

具体测量和完整工作区的未通过项见 [验证记录（工作区资料，未随文保存）](sources.md#workspace-709b0570c64c)。
保留来源的好处是能定位差异、重新生成及审查；它不提高原始厂家网格分辨率，也不会补足物理标定。

## 跨引擎兼容性为何需要另验

[OpenUSD 物理 schema](https://openusd.org/release/api/usd_physics_page_front.html)
定义刚体、关节、质量和碰撞等数据表达。格式能表示这些数据，与求解器如何实现和读取它们是两件事。
[上游概念映射](https://github.com/newton-physics/urdf-usd-converter/blob/bc8b7f06fc899a241b4ded968aecece040547915/docs/concept_mapping.md)
也列出了 effort、标定、软限位等映射缺口或扩展处理，不能把保存的 custom attribute 当作强制执行能力。

本次输出含层级刚体；上游 README 提醒部分采用 maximal coordinates 的消费实现可能不支持这种结构。
因此，交付 USD 可以通过标准解析器，但仍可能在指定 PhysX/其他后端中需要结构适配。
未来若展开层级或重定向 body 关系，须另存消费端派生层，重新检查世界变换、局部关节帧、
质量/惯量及驱动，不能直接沿用当前数值验证结论。还要单独验证 Newton 扩展的解释与速度/effort 执行。

本次取消默认单凸包和 ACOne 新增固定根，是为了让转换结果忠于源语义，
并不宣称源非凸网格已经适于动态接触。需要碰撞分解时，要记录算法、参数、派生几何及间隙误差，
再运行引擎接触测试；不能用调增益掩盖碰撞近似带来的阻挡。

## 与 usd-brep 的分工

URDF 链已有机器人结构与物性；BREP 链的优势在于具有可靠 CAD 时保留精确几何并可控离散。
本次两款资产只有已离散的 DAE/STL，逆向拟合不能恢复丢失的设计信息，
且 BREP 几何工具不负责补全机器人关节语义。
因此当前采用已验证的 URDF 派生路线，未来在有逐 link CAD 和明确精度需求时再评估 BREP 几何层。
本机源码与独立 wheel 的验证范围、球体容差异常及数据见
[usd-brep 对比与实测（工作区资料，未随文保存）](sources.md#workspace-158fd289bedd)。

## 资料范围与维护

查阅日：2026-10-15。转换器 README、映射、更新日志与 benchmark 固定到
`bc8b7f06fc899a241b4ded968aecece040547915`；Seeed 案例固定到
`158f87317fcaa35a7d1706ef364e324d3565939e`。这两个提交识别背景资料，
本次构建实际仍以资产配方记录的 PyPI wheel/依赖哈希为准。
Isaac Sim / Isaac Lab / OpenUSD 链接为查阅日的动态文档，不作为已运行引擎版本的证明。
更新工具、schema、厂家输入或目标后端时，重新核查相应依据并执行受影响的数值与运行验收。
