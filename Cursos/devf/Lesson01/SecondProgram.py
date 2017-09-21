def get_sentence():
    return 'The sum of {} and {} is {}.'

def sumProblem(x,y):
    sum= x + y
    sentence = get_sentence().format(y,x,sum)
    print(sentence)

def hola():
    sumProblem(2,3.5)
    sumProblem(100,200)
    a = int(input("enter an integer: "))
    b = int(input("enter a second integer: "))
    sumProblem(a,b)

hola()
