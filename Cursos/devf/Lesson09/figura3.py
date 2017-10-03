class Figura(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def calcuar_area(self, area):
        print "El resultado es ", area


class Cuadrado(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        resultado = self.base * self.altura
        Figura.calcuar_area(resultado)
#
# class Circulo(Figura):
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#
#     def calcuar_area(self, base, altura):
#         area = (base * 3.14159)**2
#
#
# class Triangulo(Figura):
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#
#     def calcuar_area(self, base, altura):
#         area = (base*altura)**2
#


figura_1 = Figura()
figura_1.calcuar_area(2,3)
print figura_1.__dict__