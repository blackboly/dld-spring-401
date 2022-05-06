`include "3IN.sv"
`include "xnor.sv"
module GL(input g, a, b, output G);
    wire b_b, y1, y2, y3;
    NOT not1(b, b_b);
    NAND n1(a, b_b, y1), n2(a, g, y2), n3(g, b_b, y3);
    IN3 in3(y1, y2, y3, G);
endmodule
