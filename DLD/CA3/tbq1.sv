`timescale 1ns/1ns
`include "q1.sv"
module tb();
    logic [15:0]a, b;
    logic [2:0]opc;
    logic c, d;
    wire [15:0]w;
    ALU alu(a, b, c, opc) 