import math

pi = math.pi

def area_of_cicle(radius: float):
    return pi * (radius ** 2)

r = float(input("Radius~ "))

area = area_of_cicle(r)

print(area)

input()
