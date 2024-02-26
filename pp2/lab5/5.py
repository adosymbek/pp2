#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

s = input()
x = re.findall('a(.+)b$', s)
print(x)
if x:
    print("There is a match")
else:
    print("None")