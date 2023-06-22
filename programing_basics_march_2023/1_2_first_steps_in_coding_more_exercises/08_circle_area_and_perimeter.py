from math import pi

radius = float(input())

area = radius * radius * pi
perimeter = 2 * radius * pi

print(f"{area:.2f}")
print(f"{perimeter:.2f}")