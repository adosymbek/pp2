#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

for i in range(65,91): 
    with open(chr(i)+'.txt', 'x') as f: 
        f.write("Hello world")