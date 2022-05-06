`include "q2d.sv"
module Q3 (input [15:0]a, input [15:0]b, input l, e, g, output L, E, G);
    wire J[8:0];
    Q2d r0(a[3:0], b[3:0], l, e, g, J[0], J[1], J[2]);
    Q2d r1(a[7:4], b[7:4], J[0], J[1], J[2], J[3], J[4], J[5]);
    Q2d r2(a[11:8], b[11:8], J[3], J[4], J[5], J[6], J[7], J[8]);
    Q2d r3(a[15:12], b[15:12], J[6], J[7], J[8],L, E, G);

endmodule