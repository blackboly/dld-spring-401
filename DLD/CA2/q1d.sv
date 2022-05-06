module Q1d(input a, b, l, e, g, output L, E, G);
    assign#15 L = (a<b)? 1'b1:
                (a>b)? 1'b0:l;
    assign#20 E = (a<b)? 1'b0:
                (a>b)? 1'b0:e;
    assign#15 G = (a<b)? 1'b0:
                (a>b)? 1'b1:g;
    
endmodule
    