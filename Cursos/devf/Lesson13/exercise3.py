# Program que calcular la longitud de una string_new


class Main(object):
    def __init__(self):
        running = 1
        string_new = []
        while running == 1:
            string_new = str(input('Enter <Carriage return> only to exit: '))
            if string_new == '':
                running = 0
            else:
                Calculate(string_new)
                break


class Calculate(object):
    def __init__(self, list_new):
        self.list_new = list_new
        self.count = 0
        for x in range(len(self.list_new)):
            self.count = x + 1
        print("The size of the string is", self.count)


Main()


# a = []
# prompt = "Type the string: \n"
# line = input(prompt)
#
# while line:
#     a.append(str(line))
#     line = input(prompt)
# print(a)
#
#
# running = 1
# string_new = []
# while running == 1:
#     string_new = str(input('Enter <Carriage return> only to exit: '))
#     if string_new == '':
#         running = 0
#     else:
#         break
#
# print(string_new)
# print(len(string_new))
#
