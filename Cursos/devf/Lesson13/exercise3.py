# Program que calcular la longitud de una cadena


class Calculate(object):
    def __init__(self, list):
        self.list = list
        self.count = 0
        for x in range(len(self.list)):
            self.count = x + 1
        print("The size of the string is", self.count)


list_1 = ['h', 1, 20, 'homero', 345]

Calculate(list_1)

