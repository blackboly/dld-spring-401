module oai(input a,b,c, output w);
    assign w = ~((a|b)&c);
endmodule