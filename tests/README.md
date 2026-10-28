# 验证目录

`tb_and_gate.v` 与 `test_repository.py` 用于仓库启动自检；它们不是学习验收证据。项目自己的测试以后放在 `tests/Pxx/` 并写明运行命令。

优先级：正常值 → 位宽/负数/边界 → reset/enable/valid → 随机回归 → 周期/吞吐/性能测量。Testbench 必须在 mismatch 时返回失败，不能只有波形截图和 `$display`。

GitHub Actions 运行 Python unittest 和示例 Icarus 仿真。FPGA/ASIC 设备/EDA 工具的实验需要另附机台与工具版本记录，CI 不自动代替真实上板。
