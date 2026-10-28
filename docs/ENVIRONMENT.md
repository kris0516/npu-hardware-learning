# 学习环境与工具（2026-10-28 初始计划）

## 工作站

- Apple Silicon Mac、VS Code、Python 3.12（如可用）、Git、Jupyter、KiCad。
- P01 浏览器/Nand2Tetris 即可；不要求一开始安装 Quartus。
- P03–P05 RTL：Icarus Verilog (iverilog/vvp)、Verilator、GTKWave（按实际 Mac 支持情况选择）；Python unittest + NumPy Golden Model。
- P06：目标板 Terasic DE1-SoC (Intel/Altera Cyclone V)；对应 Quartus 工具需在受支持的 Windows/Linux 机器上运行，首选 UKM 设备/工作站。
- P08：Yosys / OpenROAD / KLayout + 许可证允许的公开 PDK；可复现的开源流程不等于工艺厂 signoff。

## 安装策略

在教学会话中，初次安装与报错诊断**每次只给一条终端命令**，根据输出选择下一条；不要凭本文件假定工具已经安装。每项目第一步都做环境检查并记录真实版本。尽量先仿真再上板，避免安装过重的工具干扰早期学习。

## 文件组织

- `rtl/P03/`、`rtl/P04/`、`rtl/P05/`：学生亲自实现核心 HDL。
- `tests/Pxx/`：RTL 测试、Python Golden Model、运行器。
- `notebooks/masters/`：教师发布的只读母版；`notebooks/work/`：学员本地练习稿，通常不推送。
- `projects/Pxx-*/evidence/`：经过脱敏与复核的报告、截图、波形摘要。不要提交超大波形、二进制 bitstream、商业 PDK、API keys。
- `templates/`：复用项目交接、实验报告与小步验收模板。

## 执行与测试

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
iverilog -g2012 -s tb_and_gate -o /tmp/npu-and-gate rtl/and_gate.v tests/tb_and_gate.v
vvp /tmp/npu-and-gate
```

仓库当前的 `and_gate` 是 **CI smoke test**，不能作为完成 P01 的证据。具体项目的实际运行命令应写进该项目 README / evidence 报告。设备被锁、付费或受许可限制时只做被允许的步骤。
