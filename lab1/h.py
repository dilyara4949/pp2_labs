s = input()
t = input()
ans, cnt= '', 0
for i in range(len(s)):
    if s[i] == t:
        if cnt == 0:
            ans += str(i) + ' '
            first = i
            last = i
            cnt += 1
        else:
            cnt += 1
            last = i
if last != first:
    ans += str(last)
print(ans)
