# 协议、零位、双臂控制与源码核查

> 阶段快照：原研究日期 2026-10-16；本次仅迁入总结并整理阅读链接，未重新执行原研究的计算、仿真或真机测试。
> 原文中的下载、文件数和检查结果描述原研究工作区。`WORKSPACE/` 表示原工作区逻辑根目录；正文中的脚本命令不在本笔记包执行。
> 原源码引用已尽量转为固定提交；未收录资料的链接明确标为“工作区资料”，来源、哈希和获取边界见 [来源说明](../sources.md)。

## 1. 兼容性需要逐层核对

CAN 物理层、CAN 帧、厂家命令、数值范围、USB 桥接封包、整机 SDK 是不同层。共同采用 MIT 控制形式，不保证命令 ID、反馈 ID、量化范围或力矩单位相同。

| 层 | 必查项 | 当前结论 |
|---|---|---|
| 接插件 | 电压、地、CAN_H/L、屏蔽 | 不按外形推定 |
| 总线 | Classic CAN/CAN FD、波特率、标准/扩展帧 | 需与适配器/固件配套 |
| 电机命令 | 使能、失能、零位、反馈和模式 ID | 方舟与 Seeed 不能原样套用 |
| 数值 | rad/deg、Nm/A、P/V/TMAX、方向 | 存在已查明差异 |
| 主机桥接 | SLCAN、SocketCAN、DM serial、专用 SDK | 不是统一接口 |
| 整机模型 | 关节排序、frame、夹爪、限位 | 必须适配 |

方舟官方脚本使用 `slcand -s8`，其设备被绑定为主机 CAN 接口；Seeed DM YAML 使用 `/dev/ttyACM0` 和达妙串口桥。MotorBridge 又区分 `socketcan`、`dm-serial`、`dm-device`。文件证据已保存在本地，见源码搜索与 [来源表（工作区资料）](../sources.md#artifact-0fc163fa7eda)。

## 2. 达妙协议的文件级核查

原文件：[protocol.rs](https://github.com/motorbridge/motorbridge/blob/e2607dc1063bbcfa5ce8433644e6eb6fe8267525/motor_vendors/damiao/src/protocol.rs)、[motor.rs](https://github.com/motorbridge/motorbridge/blob/e2607dc1063bbcfa5ce8433644e6eb6fe8267525/motor_vendors/damiao/src/motor.rs)。

- MIT：8 字节，位置 16 bit；速度、Kp、Kd、转矩各 12 bit；按型号的 P/V/T 范围量化。
- POS_VEL：位置和速度上限为两个 little-endian float，CAN ID 为 0x100+电机 ID。
- VEL：速度 float，ID 为 0x200+电机 ID。
- FORCE_POS：位置 float、速度与电流/转矩比例字段，ID 为 0x300+电机 ID；比例不是精确恒定输出力。
- 当前 MotorBridge 4310 范围为 P=12.5、V=30、T=10；4340/4340P 为 P=12.5、V=10、T=28。它们是该代码版本的编解码范围，不是机械持续能力。

不要用旧说明书的 VMAX 或其他 SDK 常量覆盖实际固件参数。先读取并备份电机配置，固定控制模式和版本，再做离线编解码核对。

Stanford ARX SDK 的发送路径会区分 EC 与 DM，并对某些力矩量乘除常量；因此，即便参数都叫 torque，也不能假定直接转发数值。详见 [controller_base.cpp](https://github.com/real-stanford/arx5-sdk/blob/c160db7834530a3d80fec524547c74e1d4fa8035/src/app/controller_base.cpp) 的 `send_recv_()`。

## 3. 本轮发现的上游集成问题

这些是固定源码快照的静态核查结果，不是已测量的真机故障；未修改上游原文件。

关键定位：follower第705行计算vel_rad、第737行发送常数32；SDK YAML第36/51/66行配置Kd=8；MotorBridge protocol.rs第6行KD_MAX=5、第46行clamp；SDK pyproject.toml第6行Python范围、第13行MotorBridge仅设最低版本。行号对应本轮固定提交。

### U01：LeRobot DM 分支将速度上限硬编码为 32

文件：[seeed_b601_follower.py](https://github.com/Seeed-Projects/lerobot-robot-seeed-b601/blob/0da1a1a5575905d77823227003ffee7672059780/lerobot_robot_seeed_b601/seeed_b601_follower.py)。

`send_action()` 读取 `pos_vel_velocity` 并从 deg/s 转为 rad/s，但普通 DM 关节发送使用 `motor.send_pos_vel(pos_rad, 32)`，没有使用计算出的 `vel_rad`；夹爪使用的是另一路 FORCE_POS。

影响：修改配置中的普通关节速度可能不控制实际发送的 POS_VEL 速度上限；日志显示配置速度也不足以证明发送值正确。32 在这一接口的语义为 rad/s 上限，不是 32°/s，也不保证电机会真正达到该转速。

接入前：在自有适配层改为明确单位的已限幅速度值，验证发送帧和配置一致；确认没有其他状态分支绕过。修复建议是使用经过校验的 `vel_rad`，而非直接复制默认大值。不能以该未审核版本直接进行无人看护动作。

### U02：MIT Kd 配置 8，编码器上限 5

文件：[rebotarm_dm.yaml](https://github.com/Seeed-Projects/reBotArm_control_py/blob/6415d43130d1e143c70dc106096a857ac5556f81/config/rebotarm_dm.yaml) 的 J1–J3 MIT kd=8；本轮 MotorBridge `protocol.rs` 的 KD_MAX=5，`float_to_uint` 使用 clamp。

如果这两个快照版本配套并走该 MIT 编码路径，发送值会被限制到 5，配置和实际阻尼不一致。POS_VEL 路径不会因此自动带有 MIT 阻尼。应固定可验证的软件组合并显式设置合法增益；本轮未推定出最优增益或修改固件。

### U03：Python 版本要求存在冲突

下载的 `reBotArm_control_py/pyproject.toml` 声明 >=3.10,<3.12；网页教程使用 Python 3.12。不能同时声称该固定提交按包元数据完整支持 3.12。应选择可安装且测试过的运行版本，或者在独立环境验证并修订打包范围。本项目的 .venv 是 CAD/资料分析环境，不是已部署的机器人控制环境。

### U04：关节限位与方向不统一

DM URDF、LeRobot 与课程资料限位不同。LeRobot `joint_directions` 还包含非单纯 ±1 的夹爪系数；不能把它当成 URDF 到电机的一套全局映射直接使用。确认每个变量处在 motor/model/policy 哪层。

### U05：模型、BOM、STEP 的版本口径

README 文件名、实际目录、两个 STEP 实体数量与装配姿态不同；公开 BOM 也说明出货细节可能变化。购买前应确定硬件版本；安装孔/零位必须按实际组件确认。

## 4. 零位与安全 home

维护三层角度：电机反馈、模型变量、策略/遥操作变量。模型映射通常写为 q_model = s·theta_motor+b；夹爪使用独立函数 width=f(theta)。一旦采用非线性连杆或其他传动，不能继续假设线性。

电机保存零点、URDF q=0、碰撞安全 home、主臂校准和策略归一化是不同操作。已有 ACOne 先备份配置、读取日志，不为了比较而重置原机零点。校准是有意执行的维护步骤，不能在每次双臂启动时偷偷改写从臂 EEPROM。

原始标定记录字段：关节、方向、offset、物理限位、软限位、初始姿态照片、固件、参数导出文件、工具与日期。左右两侧分别保存。

## 5. 双总线和时序

估算假设：每电机每周期 1 命令+1反馈、每帧约130bit、经典CAN 1Mbps，未计重发/额外查询。单臂7电机250Hz约45.5%，500Hz约91%；双臂共线500Hz约182%。真实负载需要测量。

第一版左右独立总线，可保留各自 1–7 ID；主机按设备序列号绑定 left/right。若共线，必须统一改命令/反馈 ID 并评估带宽，这通常没有必要。

控制任务应共享单调时间轴，按目标执行时刻采样、插值、下发；物理 CAN 帧依次传输，不能声称“完全同时”。记录每轴反馈时间，必要时插值到统一观测时刻。控制周期、P99 抖动、反馈年龄、双臂差值、相机时间偏移分别测量。

起步可采用稳定100–250Hz位置控制，图像/学习层约30Hz，规划与推理频率依模型实测；这些是设计候选，不是已实现指标。YAML 的 rate=500、一个循环里控制两臂、两个 Python 进程都不能作为实测同步证据。

## 6. 软件结构

```text
策略/任务规划/遥操作
          ↓ 带时间戳的目标
双臂协调、限位、防碰撞与动作仲裁
          ↓
左/右单臂适配：关节排序、方向、offset、夹爪、单位
          ↓
各自通信驱动 → CAN → 电机内部闭环
```

整机模型使用 left_/right_ link 和 joint 前缀；namespace 只能解决 ROS 名称的一部分，不能自动修复 TF/frame 冲突。配置 left_arm、right_arm、both_arms、两夹爪规划组，共享桌面、立柱、头架碰撞场景。两个单臂单独避障不能防止彼此相撞。

状态机建议：OFF、CONNECTED、CALIBRATION_REQUIRED、READY、ENABLED、EXECUTING、FAULT、STOPPING。每种模式规定新命令处理、超时、掉线、过热、恢复与人工介入条件。急停复位后不自动继续旧轨迹。

防坠审计进一步发现固定版SDK的estop直接失能，重力补偿启动有0.1s失能窗口，无state时位置会补零；这些不适合作为悬空承重的安全控制依据。应把停车、制动承重交接、动力隔离及独立捕获分为明确状态，健康驱动减速与驱动失控/失电分别处理。不能用“大Kd”、取消TIMEOUT或反复clear_error/enable代替机械防坠。证据、急停时序及改造边界见[防坠专题](15_fall_prevention_and_emergency_stop.md)。

## 7. 逐级控制能力

先位置控制和低速轨迹，再重力补偿和柔顺。加装相机/夹指后更新末端质量、质心、TCP、碰撞与惯量。URDF 惯量不等于实测辨识值。

两臂共同抓同一物体时，需要相对位姿约束与柔顺；两个强位置环可能因几毫米误差互相对抗。接触装配优先考虑主从柔顺、物体坐标系规划及触觉/力反馈。电流估计转矩受摩擦、回差和参数影响，不等价于六维力传感器。

## 8. 离线与真机检查边界

本轮已完成解析、校验、模型预览与源码核查；未证明 CAN 实测频率、真机 FK/IK 精度、碰撞距离、故障停机或长期热稳定。详细验收方法见 [实施路线](06_build_and_validation_plan.md)。
