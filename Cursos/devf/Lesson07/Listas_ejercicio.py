# -*- coding: utf-8 -*-


def tamanio_cadena():
    tamanio = int(input("De que tamaño quieres hacer tu cadena: "))
    crear_cadena(tamanio)

def crear_cadena(a):
    lista = []
    for i in range(a):
        lista.append(raw_input("Proporciona la cadena: "))
    print " La lista creada es: ", lista

tamanio_cadena()

