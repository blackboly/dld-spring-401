`timescale 1ns/1ns
`include "OAI1.v"
module OAI1T();
    reg a = 0, b = 0, c = 0;
    wire w;
    OAI1 uut2(a,b,c,w);
    initial repeat(5)#90 a = ~a;
    initial repeat(8)#64 b = ~b;
    initial begin
        $dumpfile("OAI1T.vcd");
        $dumpvars(0,OAI1T);
        repeat(11)#52 c = ~c;
        $display("test complate");
    end
endmodule