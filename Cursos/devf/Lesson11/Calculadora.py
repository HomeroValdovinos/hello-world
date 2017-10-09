import math

class Calculadora(object):
    def __init__(self, marca_param):
        self.marca = marca_param

    def sumar(self, numero1, numero2):
        resultado = numero1 + numero2
        return resultado

    def restar(self, numero1, numero2):
        resultado = numero1 - numero2
        return resultado

    def multi(self, numero1, numero2):
        resultado = numero1 * numero2
        return resultado

    def dividir(self, numero1, numero2):
        resultado = numero1 / numero2
        return resultado

casio = Calculadora("casio")
print(casio.sumar(4, 8))
print(casio.restar(4, 8))
print(casio.multi(4, 8))
print(casio.dividir(1, 1))
print(casio.marca)

