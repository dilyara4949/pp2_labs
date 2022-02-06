n = input()
arr = []
while n != '0':
    d, m, y = map(str, n.split())
    arr.append([d, m, y])
    n = input()


def mySort(dt):
    return int(dt[2])*100 + int(dt[1]) + int(dt[0]) * 0.01

arr.sort(key = mySort)

for i in arr:
    for j in range(3):
        print(i[j], end=' ')
    print()