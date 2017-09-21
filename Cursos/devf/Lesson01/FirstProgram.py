name="First Program"

def Suma(var1,var2):
    var3 = var1 + var2
    print(var3)

def thisAnotherFunction():
    print("This is a second function")

msg1="This is"
msg2="a Test"

def happyBirthdayEmily(the_message1,the_message2):
    print("Happy birthday to you!")
    print(the_message1)
    print(the_message2)
    print(the_message1 + " " + the_message2)
    thisAnotherFunction()
    Suma(2,3)

happyBirthdayEmily(msg1,msg2)
