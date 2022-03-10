module OAI1(input a,b,c, output w);
    supply1 vdd;
    supply0 gdd;
    wire y1, y2;
    pmos #(5,6,7) p1(y2, vdd, a), p2(w, y2, b), p3(w, vdd, c);
    nmos #(3,4,5) n1(y1, gdd, a), n2(y1, gdd, b), n3(w, y1, c);
endmodule