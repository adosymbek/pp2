#Write a Python program with builtin function to multiply all the numbers in a list

def result(l):
   res = 1
   for x in l:
      res *= x
   return res

l = list(map(int,input().split()))
print(result(l))