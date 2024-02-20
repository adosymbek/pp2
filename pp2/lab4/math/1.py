import math

def degree_to_radian(degree):
    radian = degree * math.pi / 180
    return radian

degree = float(input("Input degree: "))

radian = degree_to_radian(degree)

print("Output radian:", radian)
