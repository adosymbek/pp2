#Write a Python program with builtin function that checks whether a passed string is palindrome or not

s = input()
n = len(s)
l = []

for i in range(int(n/2)):
   if s[i]!=s[n-i-1]:
      l.append(False)
   else:
      l.append(True)

print(all(l))