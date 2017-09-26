# -*- coding: utf-8 -*-

amount = int(input("Please insert money: "))


def get_sentence():
    return 'The change returned is {}'


def f_main():
    if amount <= 5:
        printproducts()
    else:
        print("The maximum is 5 and not minor than 4!")


def calculatechange(a, b):
    return a - b


def printproducts():
    mi_tupla = ('1.candy = $2.5', '2.popcorn = $1.4', '3.gum = $4.0', '4.paper = $1.2')
    for i in mi_tupla:
        print(i)

    product = input("Which product do you want?\n")

    if product == 'candy':
        print("You choose candy")
        precioProducto = 2.5
        print(get_sentence().format(calculatechange(amount, precioProducto)))
    elif product == 'popcorn':
        print("You choose popcorn")
        precioProducto = 1.4
        print(get_sentence().format(calculatechange(amount, precioProducto)))
    elif product == 'gum':
        print("You choose gum")
        precioProducto = 4.0
        print(get_sentence().format(calculatechange(amount, precioProducto)))
    elif product == 'paper':
        print("You choose paper")
        precioProducto = 1.2
        print(get_sentence().format(calculatechange(amount, precioProducto)))
    else:
        print("Product doesn't exist")

f_main()


