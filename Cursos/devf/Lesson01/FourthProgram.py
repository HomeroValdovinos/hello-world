def get_sentence():
    return 'The sum of {} and {} is {}.'

def majorvalue():
    print ('the value is major')

def minorvalue():
    return 'is minor'

def sumProblem(x,y):
    sum= x + y
    if x > y:
        print (majorvalue())
    else:
        print (minorvalue())
    sentence = get_sentence().format(y,x,sum)
    print(sentence)

def hola():
    sumProblem(3.51,3.5)
    sumProblem(100,200)
    a = int(input("enter an integer: "))
    b = int(input("enter a second integer: "))
    sumProblem(a,b)

hola()

