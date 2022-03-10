module NOR(input a,b, output w);
    supply1 vdd;
    supply0 gdd;
    wire y1;
    pmos #(5,6,7) p1(y1, vdd, a), p2(w, y1, b);
    nmos #(3,4,5) n1(w, gdd, a), n2(w, gdd, b);
endmodule