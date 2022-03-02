'''Implement a generator that returns all numbers from (n) down to 0.'''

n = int(input())

def gen(n):
    while n >= 0:
        yield n
        n -= 1

for i in gen(n):
    print(i)