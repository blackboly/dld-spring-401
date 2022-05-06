`include "q1d.sv"
module Q2 (input [3:0]a, input [3:0]b, input l, e, g, output L, E, G);
    wire J[8:0];
    Q1d r0(a[0], b[0], l, e, g, J[0], J[1], J[2]);
    Q1d r1(a[1], b[1], J[0], J[1], J[2], J[3], J[4], J[5]);
    Q1d r2(a[2], b[2], J[3], J[4], J[5], J[6], J[7], J[8]);
    Q1d r3(a[3], b[3], J[6], J[7], J[8],L, E, G);

endmodule