#Write a Python program to split a string at uppercase letters.

import re

s = input()
x = re.findall('[a-zA-Z][^A-Z]*', s)
print(x)