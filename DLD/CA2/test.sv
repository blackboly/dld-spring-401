`timescale 1ns/1ns
// `include "q1.sv"
// `include "q1d.sv"
`include "q2.sv"
`include "q2d.sv"
// `include "q3.sv"
// `include "q3d.sv"
module test2();
    logic [3:0]aa, bb;

    initial begin 
        aa = 4'b1;
        bb = 4'b0;
    end
    logic l= 0, e = 1, g = 0;
    wire L, E, G, L1, E1, G1;
    // Q3 q3a (aa, bb, l, e, g, L, E, G);
    // Q3d q3d(aa, bb, l, e, g, L1, E1, G1);
    Q2 q2(aa, bb, l, e, g, L, E, G);
    // Q2d q2d(aa, bb, l, e, g, L1, E1, G1);
    initial repeat(5)#4500 aa = bb;
    initial begin
        $dumpfile("test1.vcd");
        $dumpvars(0, test2);
        repeat (10)#2000 bb = bb+500;
        #1000 bb = aa;
        #1000 $stop;
        $display("test complate!!!!!!!!!!!!!");
    end
endmodule      



    // logic [15:0]aa, bb;
        // aa = 4'b0;
        // bb = 4'b0;

        
// aa = 1'b0;
//         bb = 1'b0;
    // Q1 q1(aa, bb, l, e, g, L, E, G);
    // Q1d q1d(aa, bb, l, e, g, L1, E1, G1);

