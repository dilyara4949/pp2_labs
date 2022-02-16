myList = input().split()

def rev(myList):
    for i in range(len(myList)-1, -1, -1):
        print(myList[i], end=' ')

rev(myList)