# -*- coding: utf-8 -*-

tamanio = int(input("De que tamaño quieres hacer tu cadena: "))
lista=[]
for i in range(tamanio):
    palabra = raw_input("Proporciona la cadena: ")
    lista.append(palabra)
print " La lista creada es: ", lista