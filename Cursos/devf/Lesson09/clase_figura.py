class Figura(object):

        pi = 3.14159
        area = 0

        def __init__(self, lado1, lado2):
            self.lado1 = lado1
            self.lado2 = lado2

        def area_cuadrado(self):
            area = self.lado1 * self.lado2

        def area_triangulo(self):
            area = (self.lado1 * self.lado2)/2

        def area_circulo(self):
            area = (self.pi * self.lado1)**2


