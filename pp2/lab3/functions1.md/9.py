def sphere_volume(radius):
    pi = 3.14159  # or you can use math.pi for a more accurate value of pi
    volume = (4/3) * pi * radius**3
    return volume

# Example usage:
radius = 5
print("Volume of the sphere with radius", radius, "is:", sphere_volume(radius))
