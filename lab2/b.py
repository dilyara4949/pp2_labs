n = int(input())
arr = input().split()

for i in range(n): arr[i] = int(arr[i])

max_prod = arr[0] * arr[1]
for i in range(n):
    for j in range(n):
        if i != j : max_prod = max(max_prod, arr[i] * arr[j])

print(max_prod)