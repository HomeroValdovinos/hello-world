# -*- coding: utf-8 -*-

def validate(counter=1):
    name = raw_input("Please, type your name: \n")
    age = int(input("How old are you? \n"))
    if age <= 0 or age > 100:
        if counter < 3:
            print "\nThe age shoudn't be major than 100 and less than 0. Please try again!!!!"
            counter +=1
            validate(counter) #Llamada recursiva
        else:
            print "\nINVALID INFORMATION...BYE!!"
    else:
         calculate(age,name)
        # result = 2017 + (100 - age)
        # print "Tu tendrás 100 años en el año", result, "!!!!"

def calculate(age,name):
    result = 2017 + (100 - age)
    print name, "you will get 100 years old in the year", result, "!!!!"

validate()

