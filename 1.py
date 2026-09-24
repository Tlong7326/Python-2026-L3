import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

diameter = 2 * radius

print(f"Radius: {radius}")
print(f"Diameter: {diameter}")
print(f"Area: {area}")
print(f"Circumference: {circumference}")
