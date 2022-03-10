`timescale 1ns/1ns
`include "h.v"
module ht();
reg a,b =1,c=0;
wire w;
oia1 uut(a,b,c,w);
initial repeat(5)#7 c = ~c;
initial repeat(3)#11 b = ~b;
initial begin
    $dumpfile("ht.vcd");
    $dumpvars(0, ht);
    a =0;
    repeat(4)#9 a = ~a;
    $display("test complate");
end
endmodule