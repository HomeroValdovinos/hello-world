# Program to find the greater number of three


def compare(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    elif number3 > number1 and number3 > number2:
        return number3
    else:
        return False


def main():
    var1 = int(input("Type the first number: \n"))
    var2 = int(input("Type the first number: \n"))
    var3 = int(input("Type the first number: \n"))
    result = compare(var1, var2, var3)
    if result is False:
        print("The three numbers are equals")
    else:
        print("The major number is: ", result)

main()

