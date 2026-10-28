`timescale 1ns/1ps
`default_nettype none
module tb_and_gate;
  reg a, b;
  wire y;
  integer i;
  and_gate dut (.a(a), .b(b), .y(y));
  initial begin
    for (i = 0; i < 4; i = i + 1) begin
      {a, b} = i;
      #1;
      if (y !== (a & b)) $fatal(1, "AND mismatch: a=%b b=%b y=%b", a, b, y);
    end
    $display("PASS: AND truth table");
    $finish;
  end
endmodule
`default_nettype wire
