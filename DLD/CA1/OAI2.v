module OAI2(input a,b,c, output w);
wire cb, y1, wb;
nor#(10,14)n1(y1,a,b), n2(wb,y1,cb);
not#(5,7)i1(w,wb), i2(cb,c);
endmodule