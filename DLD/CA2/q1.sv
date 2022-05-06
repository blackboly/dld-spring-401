`include "ee.sv"
module Q1(input a, b, l, e, g, output L, E, G);
    EE ee(e, a, b, E);
    GL gg(g, a, b, G);
    GL ll(l, b, a, L);
endmodule