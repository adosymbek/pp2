#Write a Python program to count the number of lines in a text file.

import os

path = 'example_4.txt'

cnt = 0

with open(path,'r') as f:
   for line in f.readlines():
      cnt+=1

print(f'Total number of lines is {cnt}')