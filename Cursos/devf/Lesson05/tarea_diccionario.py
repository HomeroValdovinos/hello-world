# -*- coding: utf-8 -*-


def creating_list(counter=1):
    size_string = int(input("Which is the size of the string? \n"))
    if size_string <= 1:
        if counter < 3:
            print("\nThe string shouldn't be major than 0. Please try again!!!!")
            counter += 1
            creating_list(counter)
        else:
            print("\nINVALID INFORMATION...BYE!!")
    else:
        nombre_familia(size_string)


def nombre_familia(a):
    directorio = {}
    for x in range(a):
        name = input("Which is your name ?")
        directorio[x] = name
    print(directorio)

creating_list()
