def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = 3  
b = 7 

print("Squared numbers from", a, "to", b, ":")
for square in squares(a, b):
    print(square)
