# -*- coding: utf-8 -*-
monto = input("Please insert money: ")
def iniciar():
    if (monto <= 5.0):
        print "ok"
    else:
        print "The maximum is 5!"

def calcularVuelto(monto,precioProducto):
    return monto - precioProducto

def imprimirProductos():
    mi_tupla = ('1.candy = $2.5', '2.popcorn = $1.4', '3.gum = $4.0', '4.paper = $1.2')
    for color in mi_tupla:
        print color
    product = raw_input("Which product do you want? ")
    if product == 'candy':
        print "You chose candy"
        precioProducto=2.5
        print"El valor devuelto es: ", calcularVuelto(monto,precioProducto)
    elif product == 'popcorn':
        print"You chose popcorn"
        precioProducto=1.4
        print"El valor devuelto es: ", calcularVuelto(monto, precioProducto)
    elif product == 'gum':
        print "You chose gum"
        precioProducto=4.0
        print"El valor devuelto es: ", calcularVuelto(monto, precioProducto)
    elif product == 'paper':
        print "You chose paper"
        precioProducto=1.2
        print"El valor devuelto es: ", calcularVuelto(monto, precioProducto)
    else:
        print "Product doesn't exist"

iniciar()
imprimirProductos()
