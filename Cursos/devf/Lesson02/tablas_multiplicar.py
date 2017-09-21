# -*- coding: utf-8 -*-
def multiplicar():
    for var1 in range(1, 11):
        print "###### Tabla de multiplicar del", var1, "#######"
        for var2 in range(1,11):
            var3 = var1*var2
            print"(", var1, "*", var2, ") =", var3
multiplicar()