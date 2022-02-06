s = input()
try:  #  when input in one line
    n, x = map(int, s.split())
    arr = []

    for i in range(n):
        arr.append(x + 2*i)

    ans = arr[0]
    for i in range(1, n):
        ans ^= arr[i]
    print(ans)

except:  # when input in two lines
    n = int(s.strip())
    x = int(input())
    arr = []

    for i in range(n):
        arr.append(x + 2*i)

    ans = arr[0]
    for i in range(1, n):
        ans ^= arr[i]
    print(ans)
