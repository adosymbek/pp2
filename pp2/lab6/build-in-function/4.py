#Write a Python program that invoke square root function after specific milliseconds

#Sample Input:
#25100
#2123
#Sample Output:
#Square root of 25100 after 2123 miliseconds is 158.42979517754858

from time import sleep
from math import sqrt

x = float(input())
miliseconds = float(input())

sleep(miliseconds/1000)

print(f'Square root of {int(x)} after {int(miliseconds)} miliseconds is {sqrt(x)}')