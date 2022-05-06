`include "gl.sv"
module EE(input e, a, b, output w);
    wire y1, y2;
    XNOR x1(a, b, y1);
    NAND n1(y1, e, y2);
    NOT n2(y2, w);
endmodule
