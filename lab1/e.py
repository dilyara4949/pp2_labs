distance, cart = map(int, input().split())
if distance <= 500 and cart % 2 == 0:
    cnt = 0
    # checking for prime or not
    for i in range(2, int(distance ** 0.5)+1):
        if distance % i == 0:
            cnt += 1
    if cnt == 0:
        print('Good job!')
    else:
        print('Try next time!')
else:
    print('Try next time!')
