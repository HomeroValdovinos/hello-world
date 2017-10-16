# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
# histograma en la pantalla. Ejemplo: procedimiento ([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******


class Main(object):
    def __init__(self):
        running = 1
        self.string_new = []
        while running == 1:
            self.string_new = str(input('Type the string of numbers (Enter <Carriage return> only to exit): '))
            print("lista", self.string_new)
            if self.string_new == '':
                running = 0
            else:
                Procedure(self.string_new)
                break


class Procedure(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.print_list = []
        for x in range(len(self.numbers)):
            for y in range(int(self.numbers[x])):
                self.print_list.append("*")
            # print("imprimir intento: ", str(self.print_list[0] + self.print_list[1] + self.print_list[2]))
            print("The list is", str(self.print_list))
            self.print_list.clear()


Main()


