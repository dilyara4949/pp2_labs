# sqrt((x2-x1)^2 + (y2-y1)^2)
x, y = map(int, input().split())
n = int(input())
arr = []

def mySort(a):
    return (a[0] - x)**2 + (a[1] - y)**2



for i in range(n):
    xx, yy = map(int, input().split())
    a = list([xx, yy])
    arr.append(a)

arr.sort(key = mySort)

for i in arr:
    print(i[0], i[1])

