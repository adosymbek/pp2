def calculate_parallelogram_area(base, height):
    area = base * height
    return area

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = calculate_parallelogram_area(base, height)

print("The area of the parallelogram is:", area)