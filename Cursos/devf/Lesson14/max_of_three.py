# -*- coding: utf-8 -*-


def main_init():
    number1 = int(input("Please type number 1: \n"))
    number2 = int(input("Please type number 2: \n"))
    validate(number1, number2)


def validate(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        print "Both are equals"


main_init()
