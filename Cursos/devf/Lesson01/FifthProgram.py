def if_else_control():
    number1=5.0
    number2=5.0

    if (number1>number2):
        print "{} major to {}".format(number1,number2)
    elif (number1==number2):
        print "{} equal to {}".format(number1,number2)
    elif number1<number2:
        print "{} minor to {}".format(number1,number2)
    else:
        print"error"

if_else_control()