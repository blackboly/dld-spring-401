`include "alu.sv"
`timescale 1ns/1ns
module ALUTB();
	logic signed[15:0] A = 16'b1111111000110111;
	logic signed[15:0] B = 16'b0000000000011100;	
	logic C = 1;
	logic[2:0] opc = 3'b000;
	logic signed[15:0] outW;
	wire zer;
	wire neg;

	ALU alu(A, B, C, opc, outW, zer, neg);
	
	initial begin
		$dumpfile("alu.vcd");
		$dumpvars(0, alu);
		#50
		repeat(14) #50 begin
			A = $random($time);
			B = $random($time);
			C = $random($time);
			opc = $random($time);
		end
		$display("test complate!");
		#50 $stop;
	end
endmodule