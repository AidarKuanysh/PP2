import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

r = int(input())

circle = Circle(r)
result = circle.area()

print(f"{result:.2f}")