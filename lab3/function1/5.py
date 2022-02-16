'''Write a function that accepts string from user and print all permutations of that string.'''

from itertools import permutations

s = input()
def perm(s):
    return permutations(s)         #returns set of tuples with perm of string
k = perm(s)
mylist = []                        # to save all strings

for i in k:
    if(list(i) not in mylist):     # to avoid repetitions
        mylist.append(list(i))

for i in mylist:
    for j in i:  
        print(j, end='')           # to print like a string
    print()

