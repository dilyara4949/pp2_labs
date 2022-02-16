class Shape:
    def __init__(self):
        pass
    def printArea(self):
        print(0)

class Rectangle(Shape):
    def __init__(self,length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def printArea(self):
        print(self.length * self.width)

length, width = map(int, input().split())
ans = Rectangle(length, width)
ans.printArea()