module ALU(input [15:0]A, [15:0]B, intput C, input [2:0]opc, output logic W[15:0], output logic zer, neg);
    always @ (A, B, opc) begin
        case(opc)
            3'd0:W = A+B+C;
            3'd1:W = A+B+A;
            3'd2:W = B+1;
            3'd3:W = B/(4/3);
            3'd4:W = A&B;
            3'd5:W =B|A;
            3'd6:~B;
            3'd7:W = 16'b0;
        endcase
    end
    always @ (A, B, opc, W) begin
        neg = W[15];
        zer = (W == 16'b0)?1:0;
    end

endmodule