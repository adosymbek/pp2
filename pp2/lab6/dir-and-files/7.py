#Write a Python program to copy the contents of a file to another file

import os

with open('example_2.txt','r') as f:
   for line in f.readlines():
      with open('copy_example_2.txt','a') as new:
         new.write(line)