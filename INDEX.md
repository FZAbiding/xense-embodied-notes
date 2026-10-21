# 全部笔记

<!-- 自动生成；请修改主题元数据后运行 scripts/check_notes.py --write-index。 -->

| 分类 | 主题 | 阶段摘要 | 原研究日期 | 更新日期 |
|---|---|---|---|---|
| cad | [TacCap：STEP 转换、质量属性与负载分离学习笔记](notes/cad/taccap-inertial-properties/README.md) | 整理主从夹爪刚体分组、STEP到URDF、质量/质心/惯量及转接件负载分离，保留方案与实测边界。 | 2026-10-12 | 2026-10-22 |
| cad | [URDF → USD：来源、完整惯量与消费端验收复盘](notes/cad/urdf-usd-conversion/README.md) | 保留0.3.3转换路线及USD来源审查，记录FR3惯量、Rizon4R碰撞和资产版本差异，动力学待验。 | 2026-10-15 | 2026-10-22 |
| humanoid | [RoboParty RP1：机械结构、执行器与算法阶段总结](notes/humanoid/roboparty-rp1/README.md) | 围绕制造版本、运动链、执行器和策略接口整理RP1研究结论及证据边界。 | 2026-10-16 | 2026-10-16 |
| rl | [灵巧手转笔：LEAP、Revo3 与 Wuji 的阶段实验复盘](notes/rl/dexterous-pen-spinning/README.md) | 保留往复转笔和Wuji整圈任务的版本、更正、接触审计及短时诊断，明确长时连续转笔尚未验证。 | 2026-10-20 | 2026-10-22 |
| rl | [Microduck Jump：V1–V9 奖励、恢复与验收复盘](notes/rl/microduck-jump/README.md) | 保留跳跃策略历代失败、V9恢复诊断和严格协议差异；CPU三跳状态完成仍未通过位置质量验收。 | 2026-10-11 | 2026-10-22 |
| rl | [PHP Parkour：深度学生、教师训练路线与复现边界](notes/rl/php-parkour/README.md) | 整理PHP方法和官方ONNX的MuJoCo复现，保留外部引导差异、第二块失败与未训练边界。 | 2026-10-20 | 2026-10-22 |
| vla | [VLA-JEPA：微调配方失误与 delta TCP 动作契约](notes/vla/vla-jepa-finetune/README.md) | 提炼错误训练入口和未保存checkpoint的教训，说明20D绝对TCP与14D增量动作的参考系、积分和兼容边界。 | 2026-07-03 | 2026-10-22 |
| ego | [GenRobot DAS：Ego、手部设备与训练数据调研](notes/ego/genrobot-das/README.md) | 区分DAS Ego/Fingers/Gripper/Dex/Controller的产品与数据用途，保留后处理、工位和验收问题。 | 2026-09-18 | 2026-10-22 |
| ego | [触觉手套与 Ego：采集通道、对齐与迁移方法](notes/ego/tactile-glove-capture/README.md) | 从本地HTML提炼触觉、手势、头手相对位姿和腕部视觉的分析框架，不转录未核实竞品表或内部产品方案。 | 2026-10-16 | 2026-10-22 |
| robot | [ARX / Seeed B601-DM：双臂平台研究阶段总结](notes/robot/arx/README.md) | 保留ARX/Seeed R3历史总结，新增R3.1模型重力矩、抱闸选型与急停承重交接，实机验收仍待完成。 | 2026-10-18 | 2026-10-18 |
| umi | [XTac UMI G1：视触觉数采、数据接口与验收调研](notes/umi/xtac-umi-g1/README.md) | 整理G1公开文档、固定代码/数据版本和模型接入边界，关注定位、同步、触觉收益与单位合格数据成本。 | 2026-09-19 | 2026-10-22 |
| sim | [Genie Sim：全身 IK、UMI 回放与仿真工程复盘](notes/sim/genie-sim/README.md) | 整理固定底盘 G2 的 IK 学习、UMI 回放、在线 A/B 与引擎复盘，保留 EEF 撤回、控制长尾及约束失败。 | 2026-10-12 | 2026-10-19 |
| sim | [具身操作仿真：银河通用、Sudo 与 Genesis 路线调研](notes/sim/manipulation-routes/README.md) | 保留三条操作仿真路线的资产、坐标、接触、感知、数据与控制比较，区分厂商声明和文件抽查。 | 2026-10-12 | 2026-10-22 |
| hand | [Wuji、Wave、OmniHand、Revo：四款灵巧手对比](notes/hand/four-hand-comparison/README.md) | 统一四款灵巧手的版本、结构、质量、控制和触觉比较口径，保留缺失证据与边界。 | 2026-09-23 | 2026-10-18 |
| hand | [Revo 3 与 Sharpa Wave：结构、控制与触觉对比](notes/hand/revo3-vs-sharpa/README.md) | 按具体SKU与标准Wave整理结构、驱动、控制物理量及触觉接口的历史对比。 | 2026-09-22 | 2026-10-18 |
| hand | [Wuji Hand 2：机械结构、驱动与产品边界](notes/hand/wuji-hand2/README.md) | 保留Wuji Hand 2执行器、机构、控制、热与产品化边界的阶段调研。 | 2026-09-21 | 2026-10-18 |
| teleop | [MANUS Metagloves Pro Haptic：跟踪、触觉反馈与遥操作调研](notes/teleop/manus-metagloves-pro-haptic/README.md) | 整理EMF跟踪、手套结构、反馈、数据链路和竞品证据，区分历史型号、软件许可与实物验收。 | 2026-09-21 | 2026-10-22 |
| research | [源策未来：WBI、动作专家、人体数据与全身控制调研](notes/research/archon-wbi/README.md) | 从本地π0.5出发拆解VLA与运控接口，区分源策官方路线、相关论文、参数计算和未披露数据规模。 | 2026-10-20 | 2026-10-20 |
| research | [Light-O1：全身动作表示、训练路线与公开范围调研](notes/research/light-o1/README.md) | 拆解公开Preview的Qwen3.5主干、FSQ和138维动作，区分完整视觉系统、动作生成与低层控制。 | 2026-10-20 | 2026-10-20 |
| research | [Natura-1：架构、动作专家、数据与评测调研](notes/research/natura-1/README.md) | 解释50B MoE、多模态动作建模与人类数据路线，区分公开事实、结构推导和厂商评测边界。 | 2026-10-20 | 2026-10-20 |
