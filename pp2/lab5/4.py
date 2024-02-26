#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

s = input()
x = re.findall('[A-Z]{1}[a-z]+', s)
print(x)
if x:
    print("There is a match")
else:
    print("None")