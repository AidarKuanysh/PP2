import math

#ex 1
deg = float(input())
rad = deg * math.pi / 180
print(rad)

#ex 2
h = float(input())
b1 = float(input())
b2 = float(input())
print((b1 + b2) * h / 2)

#ex 3
n = int(input())
s = float(input())
area = (n * s * s) / (4 * math.tan(math.pi / n))
print(area)

#ex 4
base = float(input())
height = float(input())
print(base * height)