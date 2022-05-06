module Q3d(input [15:0]a, input [15:0]b, input l, e, g, output L, E, G);
    assign#30 L = (a<b)? 1'b1:
                (a>b)? 1'b0:l;
    assign#(320, 40) E = (a<b)? 1'b0:
                (a>b)? 1'b0:e;
    assign#30 G = (a<b)? 1'b0:
                (a>b)? 1'b1:g;
endmodule
