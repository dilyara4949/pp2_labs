''' Create a generator that generates the squares of numbers up to some number N.'''

n = int(input())
def gen(a):
    a += 1          # in 'range(n)' indexing starts from 0 
    yield a * a

for i in range(n):
    print(*gen(i))
