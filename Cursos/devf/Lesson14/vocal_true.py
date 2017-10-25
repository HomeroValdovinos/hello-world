
class Vowel(object):
    def __init__(self, vowel):
        self.vowel = vowel
        if vowel == 'a' or vowel == 'A':
            print vowel
        elif vowel == 'e' or vowel == 'E':
            print vowel
        elif vowel == 'i' or vowel == 'I':
            print vowel
        elif vowel == 'o' or vowel == 'O':
            print vowel
        elif vowel == 'u' or vowel == 'U':
            print vowel
        else:
            print "error"


data = 'E'
Vowel(data)

