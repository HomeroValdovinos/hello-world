# -*- coding: utf-8 -*-


def tamanio_cadena():
    tamanio = int(input("De que tamaño quieres hacer tu cadena: "))
    crear_cadena(tamanio)


def crear_cadena(a):
    lista = []
    for i in range(a):
        lista.append(raw_input("Proporciona la cadena: "))
    print " La lista creada es: ", lista

    definir_palabra()
    encontrar_palabra(encontrar, lista)

def definir_palabra():
    encontrar = raw_input("Cual cadena quieres encontrar: \n")
    return encontrar

def encontrar_palabra(encontrar, lista):
    count = 0
    for y in range(len(lista)):
        if lista[y] == encontrar:
            count += 1
    print "La palabra se encontro ", count


tamanio_cadena()


#     definir_palabra(lista)
#
#
# def definir_palabra(lista):
#     count = 0
#     encontrar = raw_input("Cual cadena quieres encontrar: \n")
#     for y in range(len(lista)):
#         if lista[y] == encontrar:
#             count += 1
#     print "La palabra se encontro ", count

