# -*- coding: utf-8 -*-

def creando (intento=0):
    numero=int(input("De que tamaño deseas la cadena: \n"))
    lista=[]
    if intento < 3 :
        if numero > 1:
            for i in range(numero):
                lista.append(raw_input("Ingresa cadena: \n"))
        print "Esto trae Cadena", lista
    else:
        print "Parametro no valido, vuelve a intentar\n"
        intento -= 1
        creando(intento)
creando()