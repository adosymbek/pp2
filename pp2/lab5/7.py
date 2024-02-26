#Write a Python program to convert snake case string to camel case string.

import re

s = input()
x = re.sub('_', ' ', s).title()
print(x.replace(" ",""))