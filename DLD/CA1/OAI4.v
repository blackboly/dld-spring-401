module OAI4(input a,b,c, output w);
    assign#(10, 14) w = ~((a|b)&c);
endmodule

