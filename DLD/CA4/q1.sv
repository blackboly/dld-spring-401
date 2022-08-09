module q1(input d, clk, output logic Q);
	wire y1, y2, Qb;
	nand n1(y1, d, clk), n2(y2, y1, clk), n3(Q, Qb, y1), n4(Qb, Q, y2);
endmodule
