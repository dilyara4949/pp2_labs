class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    def dist(self, x0, y0):
        d = ((self.x - x0)**2 + (self.y-y0)**2) ** 0.5
        print(d)

x1, y1, x2, y2 = map(int, input().split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)

p1.show()
p2.show()

p1.move(1, 1)
p1.show()

p1.dist(1, 2)