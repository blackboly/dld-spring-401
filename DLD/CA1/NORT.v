`timescale 1ns/1ns
`include "NOR.v"
module NORT();
    reg a=0, b=0;
    wire w;
    NOR uut(a,b,w);
    initial repeat(13)#100 a = ~a;
    initial begin
        $dumpfile("NORT.vcd");
        $dumpvars(0, NORT);
        repeat(5)#220b = ~b;
    end
endmodule
