#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

s = input()
x = re.findall('a(b*)',s)
print(x)
if x:
    print("There is a match")
else:
    print("None")