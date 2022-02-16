''' Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!'''

import random
myNum = random.randint(0, 20)
print('Hello! What is your name?')
name = input()

def guessNum(myNum):
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    n = int(input())
    cnt = 1
    while n != myNum:
        if n < myNum:
            print('Your guess is too low.', 'Take a guess.', end='\n')
        else:
            print('Your guess is too large.', 'Take a guess.', end='\n')
        n = int(input())
        cnt += 1
    print(f'Good job, {name}! You guessed my number in {cnt} guesses!')

guessNum(myNum)




