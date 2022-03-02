'''Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.'''

n = int(input())

def gen(n):
    i = 0
    while i <= n:
        yield i
        i += 12          # if num divisible by 3 and 4, it is divisible by 12 also

for i in gen(n):
    print(i, end= ' ')