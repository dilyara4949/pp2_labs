class Shape:
    def __init__(self):
        pass
    def printArea(self):
        print(0)

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length

    def printArea(self):
        print(self.length ** 2)

n = int(input())
ans = Square(n)
ans.printArea()