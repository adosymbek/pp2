#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path

import os

path = input('Enter or copy\paste the path of one of your projects:\n')

if os.path.exists(path):
   print(path)
   for target in os.listdir(path):
      print(target)
else:
   print('Entered path does not exist. Try next time!')