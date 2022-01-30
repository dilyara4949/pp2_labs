'''If he worked less than or equal to 10 hours, output: Go to work!
If more than 10 and less than or equal to 25, output: You are weak
If more than 25 hours, but less than or equal to 45, output: Okay, fine
If more than 45 hours, output: Burn! Burn! Burn Young!'''

n = int(input())
for _ in range(n):
    a = int(input())
    if a <= 10:
        print('Go to work!')
    elif a <= 25:
        print('You are weak')
    elif a <= 45:
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')