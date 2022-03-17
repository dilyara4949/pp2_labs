s = input()
num_low = 0
num_up = 0
for i in s:
    if i.islower(): num_low +=1
    if i.isupper(): num_up +=1
print(f'num_low : {num_low}')
print(f'num_up : {num_up}')
