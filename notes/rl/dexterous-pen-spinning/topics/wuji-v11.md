> 历史文档快照：原记录日期 2026-10-20，于 2026-10-22 复制整理。文中“本次”“本仓库”和测试结果均指原研究工作区及当时范围；本轮只做归档、路径适配和知识库检查，未重新验证技术结论。来源见 [sources.md](../sources.md)。

# Wuji v11 stronger-push diagnostic — 2026-10-20

**Outcome:** v11 reached **24/24 standard and 24/24 ±0.3 N push** at iteration 2000 on the declared fixed diagnostic seeds. This improves on the inherited v10 selected checkpoint's 21/24 ±0.3 N preflight on seed `2026102101`. The user then prioritized longer uninterrupted turning; v11 was stopped normally at iteration 2082 after 3102.67 seconds of effective GPU training (68,222,976 environment steps), with no supervisor restart. The final checkpoint scored **24/24 standard and 23/24 push**, so iteration 2000 is selected. These are still 5.5-second one-turn episodes, not long-duration success; the v11 selected motion itself awaits direct human review.

| Checkpoint | Standard strict | ±0.3 N push strict | Role |
| --- | ---: | ---: | --- |
| [Selected 2000（工作区资料，未随文保存）](../sources.md#workspace-40c90811c8b8) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-8e98597a4dd5) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-d3eddb0c020d) | Best diagnostic weight |
| [Final 2082（工作区资料，未随文保存）](../sources.md#workspace-f1d4834e072b) | [24/24（工作区资料，未随文保存）](../sources.md#workspace-1d3b473aa9db) | [23/24（工作区资料，未随文保存）](../sources.md#workspace-f6cc767e7fac) | Preserve, not selected |

## Direct videos and raw evidence

- Selected: [standard three-view video（工作区资料，未随文保存）](../sources.md#workspace-6382c08eb731) and [±0.3 N push three-view video（工作区资料，未随文保存）](../sources.md#workspace-a4b1b873e11d). They are uncut first episodes; the linked metrics report every episode.
- Final: [standard video（工作区资料，未随文保存）](../sources.md#workspace-fc3e765e119e) and [±0.3 N push failure video（工作区资料，未随文保存）](../sources.md#workspace-b381c1ca9e60). The pushed first episode ends early at 4.775 s and fails full duration; the full set scores 23/24.
- [Offline review cards（工作区资料，未随文保存）](../sources.md#workspace-6df5463338ff) include human reference, selected policies and the failed final push.
- [Training status（工作区资料，未随文保存）](../sources.md#workspace-0c557113a5c8), [source manifest（工作区资料，未随文保存）](../sources.md#workspace-292b83fb6009), [lifecycle（工作区资料，未随文保存）](../sources.md#workspace-9c7f79e636f9), [full training metrics（工作区资料，未随文保存）](../sources.md#workspace-9a274b8cd5a5) and [config（工作区资料，未随文保存）](../sources.md#workspace-b37115a5c074). Source commit `9616015`; selected SHA256 `0c86119b41faed5160778fc535d8ef02ad541d1ea33f08a1362834d7bbca075c`, final SHA256 `a7ba2d5855702ce777e171c1cf2bf03a3520b1d14b734426fc84cdf4601187b4`.

The sealed unseen seed `2026101703` was not used for selection. The user's positive qualitative review concerned recent short-turn motion and authorized the next duration stage; v12 intentionally starts from the previously reviewed v10 iteration 4750, not from this unreviewed v11 weight.
