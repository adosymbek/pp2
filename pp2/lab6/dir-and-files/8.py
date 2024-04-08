#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not

import os
import shutil

shutil.copytree('topic_s', 'topic_s_mock_dir')

path = input('Enter or copy\paste the path of one of your projects:\n')

if os.path.exists(path):
   shutil.rmtree(path)
   print(f'Specified path       {path}         was deleted!')
else:
   print('Entered path does not exist. Try next time!')