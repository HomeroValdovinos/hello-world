# Identify a vowel


class MainInit(object):
    def __init__(self):
        self.vowel = str(input("Please type the character: \n"))
        if len(self.vowel) > 1:
            print("Invalid number of character")
        else:
            Vowel(self.vowel)


class Vowel(object):
    def __init__(self, vowels):
        self.vowels = vowels
        self.list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for j in range(len(self.list)):
            if self.vowels == self.list[j]:
                print("The vowel is ", self.list[j])
            else:
                continue


MainInit()


#
#
# class MainVowel(object):
#     def __init__(self):
#         string = str(input("Please type the character: \n"))
#         if len(string) > 1:
#             print("Invalid number of character")
#         else:
#             VerifyVowel(string)
#
#
# class VerifyVowel(object):
#     def __init__(self, string):
#         self.string = string
#         if len(string) > 1:
#             print("Invalid number of character")
#         else:
#             if string == 'A' or string == 'a':
#                 print("The vowel is: ", string)
#             elif string == 'E' or string == 'e':
#                 print("The vowel is: ", string)
#             elif string == 'I' or string == 'i':
#                 print("The vowel is: ", string)
#             elif string == 'O' or string == 'o':
#                 print("The vowel is: ", string)
#             elif string == 'U' or string == 'u':
#                 print("The vowel is: ", string)
#             else:
#                 print("No valid")
#
#
# MainVowel()
