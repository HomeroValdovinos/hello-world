class Main_init(object):
    def __init__(self):
        number1=int(input("Please type number 1: \n"))
        number2=int(input("Please type number 2: \n"))
        if number1 > number2:
            print "Number 1 is major than number 2"
        elif number1 < number2:
            print "Number 2 is major than number1"
        else:
            print "Both numbers are equals"


Main_init()

