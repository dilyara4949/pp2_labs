n = int(input())
num_demons, num_hunters = n, 0
demons, hunters = {}, {}

for i in range(n):                      # input for demons
    a, weakness = map(str, input().split())
    if weakness in demons: demons[weakness] += 1          # check, weakness alredy exist or not
    else: demons[weakness] = 1        

m = int(input())
for i in range(m):
    h, ability, num = map(str, input().split())
    if ability in hunters: hunters[ability] += int(num)   # check, ability alredy exist or not
    else: hunters[ability] = int(num)
    num_hunters += int(num)

for i in demons:                                          # run away from demons
    if i in hunters:                                      # check, do hunters have ability against demon
        if demons[i] >= hunters[i]: 
            num_demons -= hunters[i]
            num_hunters -= hunters[i]
        else:
            num_demons -= demons[i]
            num_hunters -= demons[i]


if 'hunter' in demons:                                    # check, do demons have weakness to 'hunter'
    if demons['hunter'] >= num_hunters:
        num_demons -= num_hunters
    else:
        num_demons -= demons['hunter']

print('Demons left:', num_demons)


