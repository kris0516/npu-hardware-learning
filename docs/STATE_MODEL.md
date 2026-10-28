# 学习状态机 v2 · 单一事实来源 learning/state.json

**所有项目与小步骤状态都放在同一个 JSON 文件中**，不要另外维护一份可能冲突的进度表。`README.md` 只提供路线，不追踪手工实时状态。

## 结构

- `schema_version`：进度文件数据结构版本（当前 2）。
- `cadence_days`：每项目的 14 天目标。
- `current_project` / `current_step` / `current_step_status`：准确的下一教学入口。
- `kickoff_date`：P01 正式开始日期；当前为 null，不能自动推断开始。
- `projects`：8 项，含 `status`、开始/通过日期与证据路径。
- `steps`：48 小步（每项 S01–S06），含 `status`、`evidence`、`passed_at`、`review_note`。
- `step_evidence`：当前步骤的便捷缓存，可空。权威验收仍在 `steps[].evidence` 中。

## 状态转换

`not_started → in_progress → needs_revision / blocked → passed`，修复后可以回 `in_progress`；审核中如有新证据可继续。`passed` 不是时间自动触发。任何已通过步骤如果发现回归 bug，应写决策日志和错误记录，在证据允许的前提下重开该项，而不是抹除历史。

## 合格更新方式

1. 先核对当前 GitHub HEAD 和状态文件内容，不以聊天讨论替代证据。
2. 学员提交实际完成物：电路/RTL、测试、波形或报告 + 能解释原理。
3. 教师审核后，设置具体 `steps[].status`；若 PASS，填真实 repo 相对路径的 `evidence[]`、`passed_at`（ISO 日期）、`review_note`（学生理解摘要+审查结论）。
4. 若所有 6 Steps 和 MVD 均通过，`projects[].status` 才可设 `passed`，填写项目证据与日期；否则按事实设 in_progress / needs_revision / blocked。
5. 同一次提交更新 `current_step`、`current_step_status`、`learning/knowledge.md`（如有掌握证据）、`docs/HANDOFF.md`，不能让两个文件指向不同的下一步。
6. push 后看 CI；失败则修复，不把绿色 CI 当成独立理解验收。

## 一致性自动检查

`tests/test_curriculum.py` 自动检查课程目录、8 个项目/48 个步骤、编号唯一、活跃指针一致、合法状态及 PASS 的基本证据链。它**无法判断学生是否真的理解，也不能替教师检查波形与实板数据**。

## 仿真 / 设备阻塞

若 FPGA 板卡不可用，P06 可以将已经通过的仿真/综合 Steps 单独标为 passed，但项目仍 blocked，不得虚构实板的 P06-S05 PASS。P07 可以继续部分软件/仿真练习，需如实注明对 P06 未完成的依赖；正式完成须实际补齐最小硬件闭环。
