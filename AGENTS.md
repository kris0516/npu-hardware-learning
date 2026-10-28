# Repo Agent Instructions（所有新对话和 Codex 先读）

本仓库用于以**学员能力培养**为目的的中文项目式硬件学习。仓库是跨 ChatGPT 对话的长期上下文；消息记忆不能取代 GitHub 实际文件。

## 每轮开始

1. 读取 `learning/state.json`、`docs/HANDOFF.md`、`docs/TEACHING_PROTOCOL.md`、`docs/ASSESSMENT.md`，以及当前 `projects/Pxx-*/README.md`。
2. 读取最新 `main` HEAD 与相关 RTL/testbench/Notebook 母版；不要假定上一个聊天的代码状态。
3. 明确当前项目、步骤、已有证据、上一轮待处理问题。若文件冲突，以 GitHub 实测和 `state.json` 为准，先更正状态。
4. 只推进一个尚未验收的小知识点，不提前跳到下一个项目。

## 不可妥协的教学边界

- **禁止自动生成学生尚未自己尝试的核心 RTL、关键布线、数据流调度或作业完整解答。** 可以先给短模板、接口、仿真框架、错误提示、或代码审查；学生尝试后可解释并修补。
- 不可把 CI PASS、自动生成代码 PASS、示例 smoke test PASS 当成学生已掌握。
- 对组合逻辑要求说明真值表/布尔方程；时序逻辑要求说明周期、复位、有效信号；MAC/阵列要求说明位宽、符号位、延迟及数据复用。
- 不虚构 FPGA 上板结果、频率、延迟、功率、面积或 ASIC 流片。
- 每当改动学习状态，必须附证据路径、学生解释摘要和具体审核结论；没有证据保持 not_started / in_progress / needs_revision。
- 不直接向主分支推送无法复现的二进制工件或商业 PDK/有许可证的 IP。

## Codex 可以做 / 不应做

可以：初始化目录、环境诊断、CI/脚本、文档整理、收集公开资料、生成非答案性质的脚手架、协助运行仿真、分析日志、指出有问题的行、制作性能对比表。

不应：替学员写全部核心答案并提交为“本人完成”，对未验证工作贴 PASS、把模拟数据标成实测、擅自跳过理解检查、修改教学进度以显得完成。

## 交付规范

- 一个 Step 原则上只教一项新知识；通常给一个不超过 15 行的关键代码片段、一个小练习、一个检查点；大段背景以链接供选读。
- 初始 Mac/EDA/硬件环境配置**每次只给一条终端命令**，等待学员反馈。平常已有环境时，拉取母版与复制工作文件分成两个独立命令块。
- 教师保存母版在 `notebooks/masters/`，学员实验在 `notebooks/work/`（默认 Git 忽略本地草稿）。正式成果、测试和证据经学员确认后放项目目录。
- 每次里程碑后更新 `learning/state.json`、`learning/knowledge.md` 和 `docs/HANDOFF.md`，必要时追加 `learning/decisions.md`，commit 文案记录 Pxx 和步骤。
- 改动核心代码时要求 self-checking testbench / golden model。未能运行的测试写明“未执行”，不要宣称通过。

详见 `docs/TEACHING_PROTOCOL.md` 和 `docs/CROSS_CHAT.md`。
