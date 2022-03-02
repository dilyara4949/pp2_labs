'''Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.'''

n = int(input())

def gen(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1
ans = []
for i in gen(n):
    ans.append(i)

print(ans)


    