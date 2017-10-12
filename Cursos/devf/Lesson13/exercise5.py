class MainInit(object):
    def __init__(self):
        list_1 = [1, 2, 3, 4]
        print(list_1)
        # Suma(list_1)
        Multi(list_1)


# class Suma(object):
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.adder = 0
#         for x in range(len(self.numbers)):
#             self.adder = self.numbers[x] + self.adder
#         print("This is the result of the addition", self.adder)


class Multi(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.multiplier = 0
        for x in range(len(self.numbers)):
            if x == 0:
                self.multiplier = self.numbers[x]
                print("self.multiplier es ", self.multiplier)
            else:
                break
            print("self.multiplier es ", self.multiplier)
            self.multiplier = self.multiplier * self.multiplier[x]

        print("Eso: self.numbers[x]", self.numbers[x])


MainInit()

