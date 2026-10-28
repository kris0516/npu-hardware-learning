# 新对话恢复协议（8 个项目每个新聊天）

## 新聊天的第一件事

用户新开 Pxx 对话时，教师应调用 GitHub 连接器实际读取：
- `README.md`、`AGENTS.md`；
- `learning/state.json`（唯一当前状态）、`docs/HANDOFF.md`（最近一次交接）；
- `docs/TEACHING_PROTOCOL.md`、`docs/ASSESSMENT.md`；
- 当前 `projects/Pxx-*/README.md` 与已存在的代码/Notebook/testbench；
- `learning/knowledge.md` 中已通过/不牢固概念；必要时看 `learning/decisions.md`。

**不应只凭聊天描述推定 GitHub 已变更。** 如出现 README、state、handoff 互相矛盾，优先仓库真实证据 + `state.json`；发现冲突时先明确修复，而不是悄悄跳过。

## 新聊天可直接复制的提示词

> 开始 npu-hardware-learning 的 Pxx 项目。先通过 GitHub 连接读取 kris0516/npu-hardware-learning 的 README.md、AGENTS.md、learning/state.json、docs/HANDOFF.md、docs/TEACHING_PROTOCOL.md、docs/ASSESSMENT.md、learning/knowledge.md 和当前项目 README，再读相关 RTL、tests 和母版。遵循每次一个知识点、首次配置一次一条命令、学生亲手实现核心 RTL、Codex 只辅助复杂操作的规则；从第一个未通过步骤教学，不要提前给完整答案。完成验收后提交 GitHub 状态和交接记录。

`Pxx` 应替换为实际 P01–P08，教师要检测与 `state.json` 是否一致；如果用户指定未来项目而缺少先修，先列缺口，不假装已完成。

## 每次小步骤结束

更新 `docs/HANDOFF.md` 的：版本/HEAD（写入时不猜最终 SHA，引用最近可核实 commit）、当前项目、当前 Step、已验证、尚未验证、下次具体任务；审核通过时再更改 `learning/state.json`，有概念掌握证据才更新 `learning/knowledge.md`。非阶段性问答可以只做必要记录，避免噪声提交。

## Pxx 完成的跨聊天交接

- 验收报告包含：输入假设、实现版本、运行命令、正常/边界/异常结果、资源或延迟（若有）、局限、学生独立解释和教师结论。
- `learning/state.json` 当前 Pxx 设为 `passed`，下一项设为 `not_started` 或 `in_progress`；与下一步保持一致；所有证据路径必须真实存在。
- `docs/HANDOFF.md` 写明可复用代码/API/位宽/时序契约、已知错误、工具版本、下一项目需要的关键知识。
- 下一聊天读取仓库即可知道前置基础，不要求用户重新描述所有历史。

## GitHub 权限与失败处理

有写权限时可直接提交；权限/CI 故障时明确错误，不得声称已经更新。不要把聊天内说过的“下一步”自动当作已完成的实际成绩。
