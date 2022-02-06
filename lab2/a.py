arr = input().split()

for i in range(len(arr)): arr[i] = int(arr[i])  # convert str to int

i, lastIndx = 0, 0

while i < len(arr) and i <= lastIndx:   # if i > lastIndx, we in position where cannot stay
    lastIndx = max(i+arr[i], lastIndx)
    i += 1

if i == len(arr):   # if while loop reached and of the array, we can reach last index
    print(1)
else:
    print(0)

