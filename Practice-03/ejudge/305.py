class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

length = int(input())
ar = Square(length)
print(ar.area())
