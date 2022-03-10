`timescale 1ns/1ns
`include "NOT.v"
module NOTT();
    reg a = 0;
    wire w;
    NOT n(a,w);
    initial begin
        $dumpfile("NOTT.vcd");
        $dumpvars(0, NOTT);
        repeat(5)#20 a = ~a;
    end
endmodule