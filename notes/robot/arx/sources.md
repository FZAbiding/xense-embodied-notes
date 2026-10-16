# 来源、版本与素材

这是原研究的阶段快照。原材料留在逻辑工作区 `cad/arx`，本笔记包只保存总结与精选图表。

原研究由 Agent 辅助完成，具体模型/作者身份未从材料中可靠确认。本轮只处理归档、阅读导航和链接，不把原结论标成重新验证。

## 固定版本的一手仓库

| 仓库 | 原研究固定提交 |
|---|---|
| [ARXroboticsX/A5](https://github.com/ARXroboticsX/A5) | [102101c40a35015e3fd9205ba8759b2e1f988e4d](https://github.com/ARXroboticsX/A5/tree/102101c40a35015e3fd9205ba8759b2e1f988e4d) |
| [ARXroboticsX/A5_beta](https://github.com/ARXroboticsX/A5_beta) | [190e2723e18030883cd01d70bafbad9125f7301a](https://github.com/ARXroboticsX/A5_beta/tree/190e2723e18030883cd01d70bafbad9125f7301a) |
| [ARXroboticsX/ARX5_beta](https://github.com/ARXroboticsX/ARX5_beta) | [6768e886935c7a8a368e4dc29adfe10a8b7ca473](https://github.com/ARXroboticsX/ARX5_beta/tree/6768e886935c7a8a368e4dc29adfe10a8b7ca473) |
| [ARXroboticsX/ARX_Model](https://github.com/ARXroboticsX/ARX_Model) | [74386441845f12af4da203843b6400951d6c5530](https://github.com/ARXroboticsX/ARX_Model/tree/74386441845f12af4da203843b6400951d6c5530) |
| [ARXroboticsX/ARX_PLAY](https://github.com/ARXroboticsX/ARX_PLAY) | [0214f0e6c02bc7601c0944e0da769a5daaa48b26](https://github.com/ARXroboticsX/ARX_PLAY/tree/0214f0e6c02bc7601c0944e0da769a5daaa48b26) |
| [ARXroboticsX/ARX_X5](https://github.com/ARXroboticsX/ARX_X5) | [c78328785ea23a81d908e1dcc551eca992f2f1e9](https://github.com/ARXroboticsX/ARX_X5/tree/c78328785ea23a81d908e1dcc551eca992f2f1e9) |
| [ARXroboticsX/ARX_all_in_one_readme](https://github.com/ARXroboticsX/ARX_all_in_one_readme) | [13df340df13420edc498d9b222ee51f9e2596fd6](https://github.com/ARXroboticsX/ARX_all_in_one_readme/tree/13df340df13420edc498d9b222ee51f9e2596fd6) |
| [ARXroboticsX/LIFT](https://github.com/ARXroboticsX/LIFT) | [006984b693967d4e6aca51952acfd7f9b8f0df64](https://github.com/ARXroboticsX/LIFT/tree/006984b693967d4e6aca51952acfd7f9b8f0df64) |
| [ARXroboticsX/R5](https://github.com/ARXroboticsX/R5) | [0620037dca100115e30b09ba55a45d43ae20bb0b](https://github.com/ARXroboticsX/R5/tree/0620037dca100115e30b09ba55a45d43ae20bb0b) |
| [Seeed-Projects/lerobot-robot-seeed-b601](https://github.com/Seeed-Projects/lerobot-robot-seeed-b601) | [0da1a1a5575905d77823227003ffee7672059780](https://github.com/Seeed-Projects/lerobot-robot-seeed-b601/tree/0da1a1a5575905d77823227003ffee7672059780) |
| [Seeed-Projects/lerobot-teleoperator-rebot-arm-102](https://github.com/Seeed-Projects/lerobot-teleoperator-rebot-arm-102) | [8514914a645f6f5cb23e941d12ceaf85bc6e5c79](https://github.com/Seeed-Projects/lerobot-teleoperator-rebot-arm-102/tree/8514914a645f6f5cb23e941d12ceaf85bc6e5c79) |
| [Seeed-Projects/reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm) | [ff6aaf59f3e2175dbff814ac2e843ee78e34d7ba](https://github.com/Seeed-Projects/reBot-DevArm/tree/ff6aaf59f3e2175dbff814ac2e843ee78e34d7ba) |
| [Seeed-Projects/reBotArmController_ROS2](https://github.com/Seeed-Projects/reBotArmController_ROS2) | [7506dc0fc5c2a7787dcb974d89d13f9f49d16d61](https://github.com/Seeed-Projects/reBotArmController_ROS2/tree/7506dc0fc5c2a7787dcb974d89d13f9f49d16d61) |
| [Seeed-Projects/reBotArm_control_py](https://github.com/Seeed-Projects/reBotArm_control_py) | [6415d43130d1e143c70dc106096a857ac5556f81](https://github.com/Seeed-Projects/reBotArm_control_py/tree/6415d43130d1e143c70dc106096a857ac5556f81) |
| [motorbridge/motorbridge](https://github.com/motorbridge/motorbridge) | [e2607dc1063bbcfa5ce8433644e6eb6fe8267525](https://github.com/motorbridge/motorbridge/tree/e2607dc1063bbcfa5ce8433644e6eb6fe8267525) |
| [real-stanford/arx5-sdk](https://github.com/real-stanford/arx5-sdk) | [c160db7834530a3d80fec524547c74e1d4fa8035](https://github.com/real-stanford/arx5-sdk/tree/c160db7834530a3d80fec524547c74e1d4fa8035) |

## 本机证据与验证边界

原报告包含用户对其 ACOne 实物的型号确认，以及本地 LeRobot 工程的静态代码审阅。它们只支持对应设备和版本，不能外推全部出厂配置。
原始内部代码、代码摘录和设备信息未迁入；公开读者不能仅依靠本包独立复核这些本机证据。其身份在下面的工作区资料表中说明。
R3 防坠/急停章节为资料与设计讨论；原研究没有宣布真机故障根因、安全等级或硬件方案已经验证。

## 随文素材

图表从原研究文件逐项复制，原图未编辑。来源逻辑路径、字节哈希与生成身份见 `provenance.json`；具体图像生成 Agent 未确认。

| 随文文件 | 生成方式 / 原始来源 | 许可状态 |
|---|---|---|
| [acone.png](assets/previews/acone.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [bi_seeed_acone_alignment_r2.png](assets/previews/bi_seeed_acone_alignment_r2.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [bi_seeed_concept.png](assets/previews/bi_seeed_concept.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [bi_seeed_concept_r1.png](assets/previews/bi_seeed_concept_r1.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [bi_seeed_interior_r2.png](assets/previews/bi_seeed_interior_r2.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [fall_prevention_energy_latency.png](assets/previews/fall_prevention_energy_latency.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [lift.png](assets/previews/lift.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [lift_mini.png](assets/previews/lift_mini.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |
| [seeed_dm.png](assets/previews/seeed_dm.png) | 原研究生成的分析图/模型预览；未在本轮重新生成；原报告固定版本模型或计算结果 | 原研究生成图；原创部分许可待仓库选择，底层模型条款仍见上游 |

## 未随文保存的工作区资料

以下条目用于解释原报告的资料依赖，**不是本仓库内的可下载附件**。路径相对于原研究目录。
需要完整复算时返回对应研究工作区；可以公开获取的源码和原始模型优先使用上方固定版本仓库。
每个哈希对应迁入时实际读取的文件；目录不计算哈希，未复制目录下文件。

<a id="artifact-92fbaf9817d2"></a>

### `data/base_integration_r2.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：3,633 字节；SHA256：`7d994326bb9b4377ba6a1df31065b16ee2d56b48139f5861f7647d2b64256940`。

<a id="artifact-3bdae16b9e04"></a>

### `data/bench_log_template.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：225 字节；SHA256：`1e8e673210ca59ce6c6c6a28ffda09607cbc901d1987748eb7c2421afc8f5c63`。

<a id="artifact-9393a91847b8"></a>

### `data/camera_calibration_template.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：196 字节；SHA256：`816e75a00ff07416f05da79936105cb9ddb789dd3726631ac75bdfa02b284e01`。

<a id="artifact-155da4954ff7"></a>

### `data/concept_layout.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,547 字节；SHA256：`8901572daf3ce2046d5b1bf8dcb8327c02c4da4ea5ea071f598aecc145761d16`。

<a id="artifact-22fad35cd915"></a>

### `data/concept_r2_validation.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：4,358 字节；SHA256：`849fc3f4a099663a784932d97ead1697f901aebf9446715199ca73c4f4021d0e`。

<a id="artifact-60de058e848f"></a>

### `data/fall_event_log_template.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：334 字节；SHA256：`5a479a5951f263732cfdc684a7016a88ca6a741cb766cba5e6117f2b3ff0d4c6`。

<a id="artifact-ad98c71d81b5"></a>

### `data/fall_prevention_acceptance_template.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,673 字节；SHA256：`5b4675bca747a3a39bffcef2f59e192d7d455f9e4949e0b0cc938a961f1f5f70`。

<a id="artifact-837ac889d7af"></a>

### `data/fall_prevention_calculations.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：3,056 字节；SHA256：`f34b5f4d660b04e56835effe38070efe54d9226e96d6e54fa7bbcb62175fc8e0`。

<a id="artifact-7598ca394f50"></a>

### `data/fall_prevention_code_evidence.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：11,305 字节；SHA256：`94fe9cfeb305f62446921f090d931e23c9a95dd75330dfb707889f187bdb4065`。

<a id="artifact-2c257458dcdb"></a>

### `data/fall_prevention_validation.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：3,246 字节；SHA256：`0b9d67d68aa950a6c75f64ec1b433ddaaae45a6e580294484ff81b36de901b4d`。

<a id="artifact-a40d7c50c50e"></a>

### `data/free_point_latency_examples.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：162 字节；SHA256：`e7561c3ecf246b7a2f5dc154c7a8cdd5d022bb9ae68de17f216474dbdeb26bc0`。

<a id="artifact-5b65eb4e8e90"></a>

### `data/height_comparison.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,244 字节；SHA256：`5e99a87c1da610dcb89768297c12bc5f6f233883d3c9073664a6a34e37fdfc4d`。

<a id="artifact-a2e01a3edcea"></a>

### `data/height_comparison_r1.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,153 字节；SHA256：`aaa80d59590b07a9edcd1fd945c7f0469e0692b9b49467e239cbc06ff859443f`。

<a id="artifact-91922c5496cb"></a>

### `data/joint_calibration_template.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：569 字节；SHA256：`98213458d6c377550e0670b32960eaac708de568ae6f294af4efd54399df07b4`。

<a id="artifact-8a0d4609ab96"></a>

### `data/lift_archive_manifest.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：13,020 字节；SHA256：`c7f66f9df8dccf3f2f09b635d1b7ad5900efb76c84e0b4aaa570f20c37e98505`。

<a id="artifact-7e5fd3b7869c"></a>

### `data/lift_joint_parameters.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：8,675 字节；SHA256：`8b70b482cb53fa46c10351e666aeafbb16a1307d9426dcc304ed08169c9902b2`。

<a id="artifact-2d0cab03b454"></a>

### `data/lift_model_analysis.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：36,002 字节；SHA256：`f5da04a261ea85873f1071509deda0e1134889ba3b20626708e5bc63f27cc6e4`。

<a id="artifact-04262050a10b"></a>

### `data/lift_source_manifest.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：218,695 字节；SHA256：`e6a5dbe8c2d4c072cffaeffbeb0657a23a5cdc2fc1c6e2555cbb21881ef7b0ad`。

<a id="artifact-e98f30629726"></a>

### `data/power_buffer_examples.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：329 字节；SHA256：`c7a7f5bf45c8a3dd5ba551111010e4d7f53359fc9717ee7028e85500975d6c13`。

<a id="artifact-fe9d409f9a7b"></a>

### `data/project_bom.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,693 字节；SHA256：`d691618a91e7ef8eb20761d8054ab3d529e2e78eeda65746f6fe30fc95da8cbd`。

<a id="artifact-fdcf35538ded"></a>

### `data/reach_comparison.csv`

收录状态：留在原研究工作区，本包未携带。
原文件大小：669 字节；SHA256：`6b45dca0855faa1a93c0fe5f8de0d5054b2bb7bd580357fbaa9a16c3dbb178e6`。

<a id="artifact-be8c39a9bb5a"></a>

### `data/reach_comparison.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：4,445 字节；SHA256：`449a0ac581e3bfece295cb409228afc35b8ce0ccb2eabeac345cbd935a656d0a`。

<a id="artifact-5665743962c8"></a>

### `data/reach_video_reference.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：304 字节；SHA256：`4ba2b8813a9cd4465675baf02f18e38468d1b7411a8a62522dcde30196cd3721`。

<a id="artifact-c721bcab198a"></a>

### `data/safety_external_references.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：9,131 字节；SHA256：`aec255ac9f3939e1f494ec4becd71b6a5f27f4c86e71eaee790fe53d70cb48fc`。

<a id="artifact-ccc9513d6ea6"></a>

### `data/source_manifest.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：2,113,664 字节；SHA256：`2593f06048fb72e577db8012e21eeabbdd4e643bcea2d38a13878fd22702e096`。

<a id="artifact-9d02b500c4ca"></a>

### `data/step_topology_audit.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：1,623 字节；SHA256：`978021c7bc2c1c0e7b1c79367db809c654892b40797f3730c2a6bcffcac10ea1`。

<a id="artifact-0fc163fa7eda"></a>

### `docs/01_sources_and_versions.md`

收录状态：留在原研究工作区，本包未携带。
原文件大小：17,094 字节；SHA256：`f61285d154d1b384804e2e71b135b3cd6ef41c58e628a9c9bab7b7fad48820d8`。

<a id="artifact-8c2789ffa4eb"></a>

### `docs/08_validation_and_reproduction.md`

收录状态：留在原研究工作区，本包未携带。
原文件大小：5,232 字节；SHA256：`6003ef5a8485f03890bf9bee75a090117ef66def9f16e62a9239b7e1b6555762`。

<a id="artifact-3901af58df2f"></a>

### `docs/09_visualization_guide.md`

收录状态：留在原研究工作区，本包未携带。
原文件大小：3,148 字节；SHA256：`737b7b5a09b1565b1eeece34deec80e7593228394845ad8726f657fc6108e073`。

<a id="artifact-a135e3561bde"></a>

### `docs/13_user_acone_code_confirmation.md`

收录状态：留在原研究工作区，本包未携带。
原文件大小：3,011 字节；SHA256：`a625360bded42cfc6eafa323dead80348d2e890c6bee2881be5b6801fbc9934e`。

<a id="artifact-7115edb0b210"></a>

### `extracted/ARXroboticsX/ARX_Model/A5/A5/A5/urdf/A5.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：8,842 字节；SHA256：`fe8a7124898f1ba421e02d5a0f65c105463cfc6f73706459cd5acc5871aaf2d7`。

<a id="artifact-d8ea9cbfc0ac"></a>

### `extracted/ARXroboticsX/ARX_Model/LIFT-mini/LIFTD/LIFTD/urdf/LIFTD.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：36,473 字节；SHA256：`1c4922efe554d956d7349e067ac8d9e598a04dc9691e37b0a8c3d10966aea269`。

<a id="artifact-aa949e0342ab"></a>

### `extracted/ARXroboticsX/ARX_Model/LIFT/lift_urdf/lift.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：30,708 字节；SHA256：`0f1cc62dbc3d96078905caeedf2636f9174c08ef66579d75966003090c6c8dd7`。

<a id="artifact-6845bccb93fe"></a>

### `extracted/ARXroboticsX/ARX_Model/X5/X5-2025/X5/urdf/X5.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：8,942 字节；SHA256：`cd88343e6c57971b6f5306f9cba6869d8a3081aeb04f15c10c56954bed3090a7`。

<a id="artifact-2d2f6ad8c3b6"></a>

### `models/bi_seeed_rebot_base_r2.step`

收录状态：留在原研究工作区，本包未携带。
原文件大小：150,963 字节；SHA256：`fc2377f3cbb17ee4dcef3e63e15e205d7562a28f972163c34a6e54ffc57615e8`。

<a id="artifact-e8fea1e1d71b"></a>

### `models/bi_seeed_rebot_concept.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：40,958 字节；SHA256：`3f40d6602f0cd6a5de50614ebee62f65775fcb1886ad7fe8b03deb0cc440118c`。

<a id="artifact-e1bfe8342f16"></a>

### `models/bi_seeed_rebot_concept_r1.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：41,411 字节；SHA256：`e1484596d0e6888d19fe1c7de14f0162d57d24f0612ea1a820aab1f57f115e0b`。

<a id="artifact-d805ce5e238e"></a>

### `models/lift/lift_mini_view.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：31,498 字节；SHA256：`aabb116ee79b1d4e241f1236ffbb009a5fc4f51596193856496e81a16b894d54`。

<a id="artifact-1b4e10e6d3e1"></a>

### `models/lift/lift_view.urdf`

收录状态：留在原研究工作区，本包未携带。
原文件大小：33,048 字节；SHA256：`42294b7357fcc2ec76c3eb2a92e3bd87f7bd4a6acb361669ab5be71ee435b496`。

<a id="artifact-b21adb4b8cea"></a>

### `references/arx5_2023_official_video_metadata.json`

收录状态：留在原研究工作区，本包未携带。
原文件大小：2,359 字节；SHA256：`324fa0357b7da8b1743caf692510f6866f3545c7735e7e1f7cff1b625ea204d7`。

<a id="artifact-0f661c0a2f4d"></a>

### `scripts/analyze_fall_prevention.py`

收录状态：留在原研究工作区，本包未携带。
原文件大小：9,912 字节；SHA256：`32bc5ef2ef2450930ed8b7afc124868202424c77449d8d49a2a82174a8690549`。

<a id="artifact-a1e97e100179"></a>

### `scripts/snapshot_safety_references.py`

收录状态：留在原研究工作区，本包未携带。
原文件大小：4,698 字节；SHA256：`a906c0a27ca8286cc23c3877ba1f63e5bcb33876acb21934f8a0640f3a99e96a`。

## 迁入记录

[provenance.json](provenance.json) 记录明确的源文件清单、原文及迁入版本哈希。
原 Markdown 的技术结论未在本轮主动改写；阅读链接、绝对路径前缀及历史快照提示已调整。
原报告 PDF/HTML、原始 CAD/模型/权重、源码、分析环境及运行日志均留在研究工作区。
仓库统一许可证尚未选择；第三方内容不因迁入而获得新的许可。
