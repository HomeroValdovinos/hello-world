# Program to find the greater number
def compare(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        return False


def main():
    var1 = int(input("Type the first number: \n"))
    var2 = int(input("Type the first number: \n"))
    result = compare(var1, var2)
    if result is False:
        print("Both values are equals")
    else:
        print("The major number is: ", result)

main()

