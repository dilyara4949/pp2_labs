'''Implement a generator called squares to yield the square of all numbers from (a) to (b).
 Test it with a "for" loop and print each of the yielded values.'''

a, b = map(int, input().split())

def gen(a, b):
    for i in range(a, b+1, 1):
        if i ** 0.5 == int(i ** 0.5):
            yield i

for i in gen(a, b):
    print(i)
