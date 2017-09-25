# -*- coding: utf-8 -*-


def creating_list(counter=1):
    size_string = int(input("Which is the size of the string? \n"))
    if size_string <= 1:
        if counter < 3:
            print "\nThe string shouldn't be major than 0. Please try again!!!!"
            counter += 1
            creating_list(counter)
        else:
            print "\nINVALID INFORMATION...BYE!!"
    else:
        original_list = []
        for i in range(size_string):
            string = int(input("Type a number: "))
            original_list.append(string)
    number2find = int(input("Which is the number you want to find? \n"))
    finding(number2find, original_list)


def finding(a, b):
    for i in range(len(b)):
        if a == b[i]:
            return True


creating_list()
