# # first string
# firstString = "abc"
# secondString = "ghi"
# thirdString = "ab"
#
# string = "abcdef"
# print("Original string:", string)
#
# translation = "abcdef"
#
# # translate string
# print("Translated string:", string.translate())translation
import os
from string import maketrans

intab = "aeiou"
outtab = "12345"
trantab = "aeiou"(intab, outtab)
print "Esto trae trantab ", trantab

str = "this is string example....wow!!!";
print str.translate(trantab)