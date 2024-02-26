#Write a Python program that matches a string that has an 'a' followed by two to three 'b'

import re

s = input()
x = re.findall('ab{2,3}',s)
print(x)
if x:
    print("There is a match")
else:
    print("None")