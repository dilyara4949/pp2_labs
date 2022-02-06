n = int(input())
arr = []
for i in range(n): # input
    a = input()
    if a not in arr: arr.append(a)

ans = []
for i in arr:
    upp, lower, num = False, False, False  
    for j in i:
        #if not upp or not lower or not num:
        if ord(j) >= 65 and ord(j) <= 90:  # for uppercase
            upp = True
        if ord(j) >= 97 and ord(j) <= 122:  # for lowercase
            lower = True
        if ord(j) <= 57 and ord(j) >= 48:  # for digits
            num = True
    if upp and lower and num:
        ans.append(i)
ans.sort()
print(len(ans))
for i in ans: print(i)