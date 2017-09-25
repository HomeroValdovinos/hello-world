# -*- coding: utf-8 -*-

def creating (counter=1):
    size_string = int(input("Which is the size of the string? \n"))
    #if size_string <= 1 or size_string != "^[\-]?[1-9][0-9]*\.?[0-9]+$": #Aquí falta evaluar que sea solo numero, no digito, no char
    #if size_string <= 1 or type(size_string) == "<type 'str'>":
    if size_string <= 1:
        if counter < 3 :
            print "\nThe string shoudn't be major than 0. Please try again!!!!"
            counter += 1
            creating(counter)
        else:
            print "\nINVALID INFORMATION...BYE!!"
    else:
        original_list = []
        for i in range(size_string):
            string = int(input("Type a number: "))
            original_list.append(string)
    first_list = []
    second_list = []
    for i in range(size_string):
        if i == 0 or i == (size_string - 1):
            first_list.append(original_list[i])
        else:
            second_list.append(original_list[i])
    print "First list", first_list
    print "Second list", second_list


creating()
