class Calculator():
    def __init__(self):
        lista = [1, 2, 3, 4]
        print lista
        Operations(lista)

class Operations(object):
    def __init__(self, list_numbers):
        self.list_numbers = list_numbers
        sum = 0
        mult = 0
        for x in range(len(self.list_numbers)):
            sum = self.list_numbers[x] + self.list_numbers[x]
            print "self.list_numbers[x]", self.list_numbers[x]
            mult = self.list_numbers[x] * self.list_numbers[x]
            print "2. self.list_numbers[x]", self.list_numbers[x]
        print sum
        print mult

Calculator()

