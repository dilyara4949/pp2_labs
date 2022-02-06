s = input()
try:  #  when input in one line
    n, x = map(int, s.split())
    ans = 0

    for i in range(n):
        ans ^= x + 2*i

    print(ans)

except:  # when input in two lines
    n = int(s.strip())
    x = int(input())
    ans = 0

    for i in range(n):
        ans ^= x + 2*i

    print(ans)

