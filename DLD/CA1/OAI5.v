module OAI5(input a,b,c, output w);
    assign#(6,9) w = ~((a|b)&c);
endmodule