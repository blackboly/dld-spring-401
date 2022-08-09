`include "nor.sv"
`include "not.sv"
`include "nand.sv"
module XNOR(input a,b, output w);
    wire y, y1, y_b;
    NANd n1(y1, y_b, w), n2(a, b, y1);
    NOR  n3(a, b, y);
    NOT n4(y, y_b);
endmodule
