n = int(input())
arr = []
while n != 0:
    arr.append(n)
    n = int(input())

for i in range(len(arr) // 2):  # not including central num, if size(arr) is odd
    print(arr[i] + arr[len(arr)-i -1], end=' ')

if len(arr) % 2 ==1:   # will print if size(arr) is odd
    print(arr[len(arr)//2])