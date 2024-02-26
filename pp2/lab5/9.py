#Write a Python program to insert spaces between words starting with capital letters.

import re

s = input()
x = re.findall('[A-Z][a-z]*', s)
print(" ".join(x))