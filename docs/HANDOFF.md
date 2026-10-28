# 当前交接快照 · 2026-10-28

**用途：**每个新 Pxx 对话的起点。`learning/state.json` 是正式进度来源，此处只提供人类可读摘要；每次完成真实步骤后维护。

## 当前准确状态

- 仓库：`kris0516/npu-hardware-learning`，默认分支 `main`。
- 当前项目：**P01 数字逻辑**；当前 Step：**P01-S01 半加器真值表与进位直觉**。
- 项目状态：**not_started（尚未验收）**。之前的聊天展示过半加器讲解/互动题，但没有收到用户独立答题/验收反馈，因此**不得标为通过**。
- 前置：有 Python/CS/ML 接触经验；尚无经证据确认的数字电路、Verilog、FPGA 熟练度；以入门者教学。
- 已有仓库代码：`rtl/and_gate.v`、`tests/tb_and_gate.v` 是 Codex 初始化的 CI smoke test，**不是 P01 已交作业**。
- 目标节奏：每 14 天尝试一个项目；项目正式开始日期待 P01 实际开课时记录，不能凭本文件日期推算完成。

## 下一轮教学只做

P01-S01：让学员自己推导 1-bit half adder 的 `A,B → Sum,Carry` 四组输入；先预测 `1+1=10₂`；答题后追问 `Sum 与 Carry 为什么是两个独立输出`；确认独立理解后才进入 P01-S02（XOR/AND 的实现）。

**暂时不要求安装工具、不授予 PASS、不自动生成全部 HDL。**

## 关键已定决策

1. 8 项最新映射：P01 数字逻辑，P02 MCU/PCB，P03 RTL ALU/FSM，P04 INT8 MAC，P05 Systolic Array，P06 FPGA，P07 量化 Tiny MLP，P08 ASIC 流程选修。
2. 每项目采用 14 天目标，必须基于证据验收；设备不可用允许明确标注 BLOCKED/PARTIAL，不能虚构实测。
3. 每个 Pxx 单独开新 ChatGPT 对话；GitHub 交接文件 + state + 项目说明保证连续性。
4. ChatGPT 教学与验收；学员做核心实现；Codex 只执行受控辅助任务。

后续交接请引用具体 commit/PR、路径、测试日志和学生证明；在本文件记录未解决问题与下一条准确命令（如果已确定）。
