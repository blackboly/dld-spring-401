`timescale 1ns/1ns
`include "q1.sv"
module q1tb();
	logic clk = 0;
	logic d = 0;
	logic q;
	q1 dl(d, clk, q);
	initial repeat(30) #5 clk = ~clk;
	initial begin
		$dumpfile("q1.vcd");
		$dumpvars(0, q1tb);
		#7 d = ~d;
		#11 d = ~d;
		#4 d = ~d;
		#14 d = ~d;
		#6 d = ~d;
		#9 d = ~d;
		#7 d = ~d;
		#8 d = ~d;
		#3 d = ~d;
		#14 d = ~d;
		#30 $stop;
	end
endmodule


