# 来源、版本与素材

## 一手来源与证据边界

本包继承2026-10-20的原调研。正文[主要资料索引](report.md#s15)保留38项来源，区分官方、论文、代码、采访和媒体。
核心依据为[Archon官网](https://www.archon.tech/)、[WBI技术博客](https://www.archon.tech/blog/whole-body-intelligence-cn)、
[EgoHumanoid-V2论文v1](https://arxiv.org/html/2609.37181v1)、
[V2固定提交](https://github.com/OpenDriveLab/EgoHumanoid-V2/tree/7f72d1c442d821e6705d4a9f234507af0b6232e4)、
[SONIC论文v3](https://arxiv.org/html/2511.07820v3)。网页和浮动分支仍可能更新，页面标注日期不证明所有文字当时已存在。
V2只是相关公开研究，不能直接代表源策商业S1/S0；厂商说明及媒体数字不等于第三方复现。

## 原研究、补写与迁入

原研究逻辑工作区为WBI，原报告名为“源策未来技术路线调研与学习报告_2026-10-20.md”。
原研究日期与迁入日期均为2026-10-20，但二者含义不同。
先前自动审批超时导致文件只落盘第1—6节；本轮先在原工作区追加同一会话已起草的第7—15节，随后捕获迁入版本。
补写没有引入新一轮联网核验、参数计算或机器人实验，不应伪装为独立验证。

[provenance.json](provenance.json)记录原六节文件、补写草稿与补全报告的SHA256、迁入版本及目标文件哈希。
迁入版本为archon-wbi-research-migration-v1。正文改名为report.md，增加历史边界，改写本机路径与未导入附件链接；技术结论及未知项保留。
只按清单复制正文、9幅被引用图片及精简参数结果；原工作区文件保留，不递归搬入工程。
原AGENTS.md是初始空目录的通用贡献说明，不作为本主题研究内容迁入；本包遵循[仓库规则](../../../AGENTS.md)和[贡献流程](../../../CONTRIBUTING.md)。

<a id="workspace-openpi"></a>
## 工作区资料：OpenPI检出与源码定位

这些是原研究实际检查过的工作区资料，不是本仓库的可下载代码附件。
逻辑工作区为xense-openpi，原检出提交为1424384a975b443eaac70b416189067a8547c94c。
[公开仓库入口](https://github.com/XenseRobotics-AI/xense-openpi)及[对应提交定位](https://github.com/XenseRobotics-AI/xense-openpi/tree/1424384a975b443eaac70b416189067a8547c94c)
用于寻找上游；本轮未重新联网确认该提交的可访问性，也未把当前main冒充本地历史版本。
原研究记录所查10个核心文件相对该本地HEAD均无修改；不表示整个工作区干净。

| 原检出中的相对逻辑路径 | 原研究记录的SHA256 |
| --- | --- |
| `src/openpi/models/pi0_config.py` | `6f6740f0011053949cb25d76e4e543b933861bfc55980c002774819ecc9d7a2f` |
| `src/openpi/models/pi0.py` | `05d328cafe06d7a1d74b2de5475642358bc02b51bd209198314cce3df6056392` |
| `src/openpi/models/gemma.py` | `5534d796b3a3b873d2fcae34c3e95b13f999b3f1efc23527a16381f321e319a0` |
| `src/openpi/models/tokenizer.py` | `965be8b3c393a6811875bbc32da9e01a5d01cc2f87802de801cf7293e049748c` |
| `src/openpi/policies/bi_flexiv_policy.py` | `a42471cd6762452792e056cf3c1d934b326cfd2ebf2a9ca848979c5bbda948ad` |
| `src/openpi/policies/xtac_umi_policy.py` | `39773e92b1d167d92bc030f30de978ae2e4d8f9f7be2831199d5e1c16be766aa` |
| `src/openpi/training/config.py` | `b5e9ec7d6b496010cd801ee2022e77464c610c8df10649e54c4d77a345740463` |
| `src/openpi/rlt/config.py` | `0f6c043bc8e415649a7c0bf71249634f838605afeeec96563cb47387eda91707` |
| `configs/_examples/pi05_base_xtac_umi_pick_up_cube_0807_h200.yaml` | `5babe784fd34c17bd8a36f5b9b3f277931d3a4d464482a4be752c7d4d37704aa` |
| `packages/xense-client/src/xense_client/rtc_action_chunk_broker.py` | `c6893bf546eb4de2d4ca2a9a84889bbed25437b4e727aba45803663a02b2db23` |

<a id="workspace-parameter-count"></a>
## 工作区资料：参数形状计算

原脚本逻辑定位为WBI/research/2026-10-20/count_openpi_parameters.py，工程脚本不随笔记发布。
原研究由本对话助手使用CPU上的flax.nnx.eval_shape统计默认Pi0Config，未加载权重，无LoRA，动作维数32、窗口50。
归档[统计摘要](assets/evidence/openpi-parameter-summary.json)仅保留配置、分组计数与总数，不导入逐参数叶节点的完整工作文件。
本轮只核对摘要与原结果、表格及加和一致，没有再次执行原计算。

<a id="workspace-code-evidence"></a>
## 工作区资料：本地代码证据

原文件逻辑定位为WBI/research/2026-10-20/local_code_evidence.json。
其中相关提交和文件哈希在本页保留；原文件包含本机定位，不原样迁入。源码、运行环境和未检查的其他工程不收录。

<a id="workspace-figure-generation"></a>
## 工作区资料：配图生成

原脚本逻辑定位为WBI/research/2026-10-20/make_figures.py。
7幅PNG教学示意或实验重绘在原工作区用Matplotlib生成；未运行AI图像生成服务。
本包仅收录正文实际显示的PNG，不重复导入对应SVG、生成脚本或未引用图片。
图框大小不代表参数量或耗时，数据曲线来自公开表格而非新增试验。

<a id="workspace-video-inspection"></a>
## 工作区资料：官方视频抽帧

原记录逻辑定位为WBI/research/2026-10-20/official_video_inspection.json。
原调研抽样查看官网短片；本包仅保留正文引用的s0_sample.jpg，原视频不随文导入。
官网[完整视频链接](https://youtu.be/b0h9oC8FhpU)在本次原调研中未能通过网页工具读取，不声称逐帧审阅完整视频。
官网卡片标题、媒体文件名和单帧画面都不足以独立证明自主性、训练配方或成功率。

## 素材来源与许可

所有素材保留原调研2026-10-20版本。本轮人工检查沿用原调研已查看的图像，另执行文件可读性和哈希检查；未新增技术实验。

| 随文文件 | 作者／生成方式与处理 | 来源／版本 | 许可与边界 |
| --- | --- | --- | --- |
| [s0_sample.jpg](assets/archon-wbi/s0_sample.jpg) | 官方视频约14.1秒处抽帧并缩小尺寸；原工作区生成 | [原始依据](https://assets.archonrobotics.tech/demo/20260930/s0.mov)；2026-10-20快照 | 原权利人许可范围未核实；不由本仓库另行授权 |
| [01_wbi_stack.png](assets/archon-wbi/01_wbi_stack.png) | 本对话助手原调研绘制的教学示意 | [原始依据](https://www.archon.tech/blog/whole-body-intelligence-cn)；2026-10-20快照 | 原创示意未单独指定许可证；不代表厂商内部架构 |
| [02_pi05_vlm_ae.png](assets/archon-wbi/02_pi05_vlm_ae.png) | 本对话助手依据本地实现绘制的教学示意 | [工作区资料](#workspace-openpi)；2026-10-20快照 | 原创示意未单独指定许可证；不发布内部源码 |
| [03_egohumanoid_pipeline.png](assets/archon-wbi/03_egohumanoid_pipeline.png) | 本对话助手依据公开研究绘制的教学示意 | [原始依据](https://arxiv.org/html/2609.37181v1)；2026-10-20快照 | 原创示意未单独指定许可证；不等于商业模型实现 |
| [04_data_flywheel.png](assets/archon-wbi/04_data_flywheel.png) | 本对话助手原调研绘制的工程解释 | [原始依据](https://www.archon.tech/blog/whole-body-intelligence-cn)；2026-10-20快照 | 原创示意未单独指定许可证；具体训练配比未知 |
| [05_multirate_control.png](assets/archon-wbi/05_multirate_control.png) | 本对话助手依据SONIC论文绘制的执行示意 | [原始依据](https://arxiv.org/html/2511.07820v3)；2026-10-20快照 | 原创示意未单独指定许可证；不是源策频率规格 |
| [06_alignment_results.png](assets/archon-wbi/06_alignment_results.png) | 本对话助手按论文Table 1重绘点估计；非新增实验 | [原始依据](https://arxiv.org/html/2609.37181v1)；2026-10-20快照 | 重绘图未单独指定许可证；数据归原研究，右图为子任务得分 |
| [07_action_interface.png](assets/archon-wbi/07_action_interface.png) | 本对话助手根据本地接口与V2规格绘制 | [原始依据](https://arxiv.org/html/2609.37181v1)；2026-10-20快照 | 原创示意未单独指定许可证；区分动作维数与参数规模 |
| [egohumanoid_v2_framework.webp](assets/archon-wbi/egohumanoid_v2_framework.webp) | EgoHumanoid-V2作者官方原图，原样复制 | [原始依据](https://opendrivelab.com/EgoHumanoid-V2/assets/figures/framework.webp)；2026-10-20快照 | 素材单独许可未核实；版权归原权利人，本仓库不新增授权 |
| [openpi-parameter-summary.json](assets/evidence/openpi-parameter-summary.json) | 从原CPU形状计算结果提取的精简摘要 | 原工作区统计；2026-10-20 | 不是权重、训练日志或厂商模型规格；本次不新增统一许可 |

## 外部与未收录资料

原始网页HTML、全文抽取TXT、页面JavaScript、上游文件树JSON及下载的第三方源码，均留在WBI工作区，仅以正文来源链接定位。
模型权重、数据集、SDK、环境、控制与训练代码不随笔记保存。未引用图片与重复SVG也不迁入。
本机独有脚本及证据只能通过原工作区获取，不伪装为公开下载资源。
未核实许可的第三方素材不由知识库代为授予；保留来源说明不等于已取得额外传播授权。

## 本轮检查与后续更新

本轮执行原文件与目标SHA256核对、9幅图片解码、参数摘要一致性、迁入边界、元数据、索引和本地链接／锚点检查。
这些属于知识库准入检查，不证明外网链接当前可用，也不重新证明公司路线、商业指标或机器人实验。
后续变更保留原始source_sha256，说明改动并更新destination_sha256；不声称自动同步原工作区后续内容。
