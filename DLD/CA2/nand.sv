module NAND(input a,b, output w);
    supply1 vdd;
    supply0 gdd;
    wire y1;
    pmos #(5,6,7) p1(w, vdd, a), p2(w, vdd, b);
    nmos #(3,4,5) n1(w, y1, a), n2(y1, gdd, b);
endmodule