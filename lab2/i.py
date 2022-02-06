n = int(input())
arr = []
ans = ''
for i in range(n):
    a = input()
    if a[0] == '1':
        arr.append(a[2:])
    else:
        if len(arr) > 0:
            ans += arr[0] + " "
            arr.remove(arr[0])
print(ans)