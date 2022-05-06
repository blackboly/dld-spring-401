`timescale 1ns/1ns
`include "OAI2.v"
`include "OAI1.v"
`include "OAI5.v"
module OAI1T();
    reg a = 0, b = 0, c = 0;
    wire w1,w2,w5;
    OAI2 uut2(a,b,c,w2);
    OAI1 uut1(a,b,c,w1);
    OAI5 uut4(a,b,c,w5);
    initial repeat(5)#90 a = ~a;
    initial repeat(8)#64 b = ~b;
    initial begin
        $dumpfile("OAI2T.vcd");
        $dumpvars(0,OAI1T);
        repeat(11)#52 c = ~c;
        #100 $stop;
        $display("test complate");
    end
endmodule