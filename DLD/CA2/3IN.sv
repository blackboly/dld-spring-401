
module IN3(input a,b,c, output w);
    supply1 vdd;
    supply0 gdd;
    wire y1, y2;
    pmos #(5,6,7) p1(w, vdd, a), p2(w, vdd, b), p3(w, vdd, c);
    nmos #(3,4,5) n1(w, y1, a), n2(y1, y2, b), n3(y2, gdd, c);
    // assign w = ~(a&b&c);
endmodule