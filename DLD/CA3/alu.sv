`timescale 1ns/1ns
module ALU(input signed[15:0] A, B, input C, input[2:0] opc, output reg signed[15:0] W, output zer, neg);
	always @(A, B, C, opc) begin
		W = 16'bx;
		case (opc)
			3'b000: W = A + B + C;
			3'b001: W = B + A+A;
			3'b010: W = B + 1;
			3'b011: W = B*(3/4);
			3'b100: W = B & A; 
			3'b101: W = B | A;
			3'b110: W = ~B;
			3'b111:	;
			default: W = 16'bx;
		endcase
	end
	assign zer = ~|W;
	assign neg = W[15];
endmodule