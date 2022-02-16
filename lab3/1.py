class Myclass:
    def __init__(self):
        self.str1 = ''

    def getString(self):
        self.str1 = input()

    def printString(self):
        print(self.str1)


s = Myclass()
s.getString()
s.printString()
