s = input().split()
ans = ''
for i in range(len(s)):
    if len(s[i]) >= 3:
        ans += s[i] + ' '
        
print(ans)
