`timescale 1ns/1ns
`include "q1.sv"

module test2();
    logic aa = 0, bb = 0, l = 0, e = 1, g = 0;
    wire L, E, G;
    GL gl(g, a, b, G);
    initial repeat(3)#330 aa = ~aa;
    initial begin
        $dumpfile("test1.vcd");
        $dumpvars(0, test);
        repeat(5)#170 bb = ~bb;
        #100 $stop;
        $display("test complate!!!!!!!!!!!!!");
    end
endmodule      