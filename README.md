# NPU Hardware Learning · 项目驱动的硬件设计课程

[![Learning repository CI](https://github.com/kris0516/npu-hardware-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/kris0516/npu-hardware-learning/actions/workflows/ci.yml)

> 从零基础数字逻辑，到 MCU/PCB、SystemVerilog、MAC、Systolic Array、FPGA 推理，再到可选 ASIC 实现。每 14 天争取交付一个可复现的小项目；**学会核心原理比按时勾选进度更重要**。

**课程语言：中文（术语附英文） · 学员环境：Apple Silicon Mac / VS Code · 硬件：UKM 实验室按申请情况使用。**

## 进入项目 / 新聊天必读

1. [当前唯一真实进度 learning/state.json](learning/state.json) — 不要根据聊天记忆推定完成。
2. [跨聊天接力 docs/HANDOFF.md](docs/HANDOFF.md) — 当前步骤、已有成果、阻塞与开课提示词。
3. [教学协议 docs/TEACHING_PROTOCOL.md](docs/TEACHING_PROTOCOL.md) — 教学小步制、学生亲手实现、Codex 分工。
4. [总路线 docs/CURRICULUM.md](docs/CURRICULUM.md) — P01–P08 依赖关系与两周节奏。
5. [验收与证据 docs/ASSESSMENT.md](docs/ASSESSMENT.md) — CI 通过不等于学习通过。
6. [面向 Codex 的 AGENTS.md](AGENTS.md)。

**新聊天入口：**打开对应 `projects/Pxx-.../README.md`；让 ChatGPT **先读取上述文件和 GitHub 当前 HEAD**，再只讲本项目的第一个未通过小步骤。不要一口气输出完整答案。

## 项目路线（每项 14 天为目标，不是已承诺完成）

| 项目 | 学习产物 | 14 天最低演示（MVD） | 关键证据 |
|---|---|---|---|
| [P01 数字逻辑](projects/P01-digital-logic/README.md) | NAND → XOR → 半/全加器 | 4-bit Ripple-carry Adder | 真值表、穷举/边界测试、亲自解释进位 |
| [P02 MCU 与 PCB](projects/P02-mcu-pcb/README.md) | ESP32 GPIO/UART 与 KiCad 小板 | 按键→LED + 串口日志 + ERC/DRC | 接线图、源文件、实物/模拟证据 |
| [P03 RTL 设计](projects/P03-rtl-datapath/README.md) | Verilog ALU、寄存器、FSM | 可综合 8-bit ALU + 同步控制 | 自检 Testbench、波形、无锁存器 |
| [P04 INT8 MAC](projects/P04-int8-mac/README.md) | 有符号定点乘加与时序 | 可复位、可使能的 INT8×INT8→INT32 MAC | Python Golden Model、边界测试 |
| [P05 Systolic Array](projects/P05-systolic-array/README.md) | PE 阵列、周期级 Dataflow | 2×2 正确矩阵乘法；4×4 为进阶 | Cycle trace、随机矩阵对照 |
| [P06 FPGA 原型](projects/P06-fpga-deployment/README.md) | 约束、综合、时序与上板 | P05 阵列板上可运行（若获设备权限） | Quartus 报告、实板记录；无设备则标部分完成 |
| [P07 量化推理](projects/P07-tiny-mlp/README.md) | Tiny MLP 端到端软硬协同 | 小型量化 MLP 推理与正确性比较 | 量化规格、端到端延迟、正确性 |
| [P08 ASIC 流程（可选）](projects/P08-asic-flow/README.md) | RTL→综合→布线→PPA | 一个 MAC/小阵列的可复现 GDSII 练习 | DRC/STA/面积/频率与限制；非真实流片 |

**路线调整说明：**仓库最初的 P01–P08 把“时序逻辑、MCU、PCB、FPGA”等拆分为不同项目。2026-10-28 起统一以上最新版编号；旧初始化示例 `rtl/and_gate.v` 与 `tests/tb_and_gate.v` **只用于 CI 烟测**，不构成 P01 验收。

## 核心规则

- 一个新知识点 / 一次练习 / 一次反馈；前置数学在需要时引入，要求写清位宽、signedness、时钟/周期。
- 教师准备路线、题目、脚手架和测试；**学员亲自实现核心逻辑**。Codex 可帮忙查资料、搭环境、检查工具、生成非核心样板、运行测试，但不得代替学员完成未学核心答案。
- **先仿真，再 FPGA，再 ASIC**；没有板卡或流片不要虚构实测结果。
- 每阶段至少留下设计文件、可复现的验证命令、实验记录、设计决策和一次口头/书面解释。
- GitHub Actions 验证代码的可执行部分；学习是否通过由 ChatGPT 按 [验收规范](docs/ASSESSMENT.md) 审核、记录证据后决定。

## 仓库结构

```text
AGENTS.md                  # ChatGPT/Codex 的协作边界
docs/                      # 课程规划、设备、交接、教学/验收规范
projects/P01-...P08-.../   # 每个新聊天的唯一项目规格
learning/state.json        # 权威进度文件；不得凭猜测改 PASS
learning/knowledge.md      # 实际概念掌握和待复习点
learning/decisions.md      # 路线与工程决策记录
rtl/                       # 可综合学生 RTL（当前仅有示例）
tests/                     # Testbench、Python 校验
notebooks/                 # 教师母版与学习练习副本
templates/                 # 步骤、实验、交接模板
.github/workflows/         # 自动化验证
```

环境见 [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md)，课程与中文教材见 [docs/RESOURCES.md](docs/RESOURCES.md)，UKM 仪器/预算见 [docs/EQUIPMENT.md](docs/EQUIPMENT.md)。

## 已有示例的基础验证

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
iverilog -g2012 -s tb_and_gate -o /tmp/npu-and-gate rtl/and_gate.v tests/tb_and_gate.v
vvp /tmp/npu-and-gate
```

首次工具安装和故障排查实行“一次只给一条命令”；不会假定学员已安装 Icarus、Quartus 或有实验室访问权限。

## 学习目标与边界

最终希望形成 **可自己解释、实现并验证的硬件设计能力**，以及实习简历可展示的仓库与测量报告。P07 最低验收是 *tiny inference demonstrator*；更完整的 64→16→10 手写数字网络、性能优化、流片均为可延长的研究目标，不应在 14 天内被误报为必成。
