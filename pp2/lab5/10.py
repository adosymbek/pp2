#Write a Python program to convert a given camel case string to snake case.

import re

s = input()
x = re.findall('[A-Z][a-z]*', s)
a = []
for word in x:
   word = word.lower()
   a.append(word)

print("_".join(a))