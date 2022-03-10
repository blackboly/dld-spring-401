module NOT(input a, output w);
    supply1 vdd;
    supply0 gdd;
    pmos #(5,6,7) p1(w, vdd, a);
    nmos #(3,4,5) n1(w, gdd, a);
endmodule