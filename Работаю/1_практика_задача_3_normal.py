import math
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c
x_1 = (-b + math.sqrt(d)) / 2*a
x_2 = (-b - math.sqrt(d)) / 2*a
print(x_1)
print(x_2)