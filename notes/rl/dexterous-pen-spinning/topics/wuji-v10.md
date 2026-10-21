> 历史文档快照：原记录日期 2026-10-20，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](../sources.md)。

# Wuji v10 completed robustness screen — 2026-10-20

**Outcome:** The two-hour effective GPU budget ended normally at iteration 5338 with no supervisor restart. The selected iteration 4750 scored **24/24 standard and 24/24 ±0.2 N push** on the declared fixed diagnostic seeds. The final iteration 5338 scored **24/24 standard and 20/24 push** on the same seeds, so final is not the selected model. This is a short 360° turn in a 5.5-second episode, not a continuous 30/60/120-second result. On 2026-10-20 the user described the recent pending motions as fairly natural and authorized longer-duration training. This is positive qualitative review of the selected short-turn motion; every new long-duration handover still needs independent review. The sealed unseen seed `2026101703` was not opened.

| Checkpoint | Standard strict | ±0.2 N push strict | Decision |
| --- | ---: | ---: | --- |
| [Selected 4750（工作区资料，未随文保存）](../sources.md#workspace-34637b59d398) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-7ede331484b9) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-5668658e6620) | Preferred diagnostic parent for v11 |
| [Final 5338（工作区资料，未随文保存）](../sources.md#workspace-d5c64cb98cf0) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-f55b0e6a0318) | [20/24（工作区资料，未随文保存）](../sources.md#workspace-1d14269e1973) | Preserve, not selected |

[User motion feedback（工作区资料，未随文保存）](../sources.md#workspace-dc9aacb3fdd7) records the exact wording and scope.

## Videos for direct motion review

- Selected 4750: [standard three-view rollout（工作区资料，未随文保存）](../sources.md#workspace-f2465e952e68) · [±0.2 N push three-view rollout（工作区资料，未随文保存）](../sources.md#workspace-4ade54897fd8). Both are uncut first episodes; the metrics files above contain all 24 episodes.
- Final 5338: [standard three-view rollout（工作区资料，未随文保存）](../sources.md#workspace-69f944dbf868) · [±0.2 N push three-view rollout（工作区资料，未随文保存）](../sources.md#workspace-7b2193132af3). The pushed video shows a real early stop at 4.0 seconds; four of 24 push episodes failed strict gates. Do not treat the final checkpoint as a robustness improvement.
- Preserved regression example: [iteration 2250 pushed rollout（工作区资料，未随文保存）](../sources.md#workspace-87ec26e5f4c8) · [24-episode failures（工作区资料，未随文保存）](../sources.md#workspace-c911c9bf6dc1). This checkpoint had 15/24 push passes and includes posture/contact failures in the 24-episode metrics; the video is episode 0, which itself passed.
- Next challenge preflight on selected 4750: [±0.3 N pushed rollout（工作区资料，未随文保存）](../sources.md#workspace-7cc19f02f1f8) · [21/24 metrics（工作区资料，未随文保存）](../sources.md#workspace-b6df66a11145), seed `2026102101`. Failures included non-pad support and an early stop with self-contact/regrasp failure in other episodes; the video is the passing episode 0.

Open the [offline review cards（工作区资料，未随文保存）](../sources.md#workspace-91e1bc814f3c) to compare the human reference, selected candidate and failures. The recorded videos use synchronized palm-side/top/side views with colored fingers. Still inspect index/middle crossing, true pad contact, release and handover, and consistency with the approved human demonstration.

## Provenance and limits

- Source commit: `c1290ac`; experiment [plan（工作区资料，未随文保存）](../sources.md#workspace-d3f51a4916f2) and [executable config（工作区资料，未随文保存）](../sources.md#workspace-2d95d0c26287).
- Selected SHA256: `beb058f8a5b82343e06311c2c606f5f8713bbcc792c84e75b90753bfe28236d3`. Final SHA256: `68fffe8fa622b6ec83f81988f9e707eba799be8fe8e690fae17604af5e08641e`.
- [Source manifest（工作区资料，未随文保存）](../sources.md#workspace-b70fb40d1fde), [training status（工作区资料，未随文保存）](../sources.md#workspace-ca0fcb8bc144), [lifecycle（工作区资料，未随文保存）](../sources.md#workspace-0207ebcc6530), [full training metrics（工作区资料，未随文保存）](../sources.md#workspace-306cb159fa10), and [supervisor finish record（工作区资料，未随文保存）](../sources.md#workspace-8e078e5543c3). Effective GPU training: 7200.14 seconds; 174,915,584 environment steps; 5338 updates.
- Strict machine gates include completion, angle, calibrated pad contact, no crossing/reverse bending, self-contact, handovers and terminal regrasp. Passing these gates does not establish human-equivalent motion. The policy still observes legacy merged distal/tip force, while acceptance uses frozen pad regions.
- v11 separately tests stronger ±0.3 N pushes from the selected weight; no duration escalation or sealed holdout is included.
