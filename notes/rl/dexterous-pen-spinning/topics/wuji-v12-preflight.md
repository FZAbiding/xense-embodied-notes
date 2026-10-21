> 历史文档快照：原记录日期 2026-10-20，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](../sources.md)。

# Wuji v12 duration-bridge preflight — 2026-10-20

The user described recent one-turn motions as fairly natural and authorized longer-duration training. The exact [feedback（工作区资料，未随文保存）](../sources.md#workspace-dc9aacb3fdd7) applies to the inherited short-turn candidate, not to an untrained multi-turn handover. Parent: [v10 selected iteration 4750](wuji-v10.md), SHA256 `beb058f8a5b82343e06311c2c606f5f8713bbcc792c84e75b90753bfe28236d3`. Scene, bank and pad map are byte-identical copies.

**Baseline: 0/24 complete two-turn passes.** The inherited policy has not learned to hand over through the first-circle boundary. All videos below are uncut first-episode rollouts, with per-episode failures in the adjacent metrics.

| Preflight | 24-episode finding | Video | Raw metrics |
| --- | --- | --- | --- |
| Raw 720° target with old command inputs | 0/24; median termination near 0.83 s | [Video（工作区资料，未随文保存）](../sources.md#workspace-ad3fe94ad986) | [Metrics（工作区资料，未随文保存）](../sources.md#workspace-718828110383) |
| Repeating one-turn command phase, global physics/angle still continuous | 0/24; median termination near 3.76 s after a complete first circle | [Video（工作区资料，未随文保存）](../sources.md#workspace-a1291033e1f6) | [Metrics（工作区资料，未随文保存）](../sources.md#workspace-11f34b05f581) |
| 450° bridge with raw command | 0/24; median termination near 0.83 s | [Video（工作区资料，未随文保存）](../sources.md#workspace-6b3e7bc8284b) | [Metrics（工作区资料，未随文保存）](../sources.md#workspace-a4e419882d19) |
| 450° bridge with repeating phase | 0/24; median termination near 3.76 s at the first additional handover | [Video（工作区资料，未随文保存）](../sources.md#workspace-49f3d9acc9f2) | [Metrics（工作区资料，未随文保存）](../sources.md#workspace-f3095def12d6) |
| 450° repeating phase, diagnostic without early grip cutoff | 0/24; median termination near 1.83 s with physical/self-contact failures | [Video（工作区资料，未随文保存）](../sources.md#workspace-2503b998a304) | [Metrics（工作区资料，未随文保存）](../sources.md#workspace-2abf92a6c4be) |

The repeating phase keeps the policy's 111-dimensional observation exactly equal to the old one-turn observation during the first turn at matched physical state; a direct parity check found maximum absolute difference 0.0. It does **not** reset pen pose, contact state, accumulated signed angle or episode time. In the 720° first episode, turn 1 reached about 364° with five stable pair handovers and a one-step maximum grip gap; the rollout then ended near 3.8 s with an index/middle posture violation and non-pad contact. These failures motivate the [450→540→630→720° training plan（工作区资料，未随文保存）](../sources.md#workspace-d7e251bbe19b).

The strict evaluator checks each completed 360° window, real pad contact, stable pair handovers, terminal regrasp and full uninterrupted duration. A model will not be called successful based on angle alone. The sealed unseen seed remains closed for model selection.
