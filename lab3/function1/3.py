''' Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
'''
numheads, numlegs = map(int, input().split())

''' 2chic + 2rab = 2numheads
    2chic + 4rab = numlegs        by this linear system'''

def findRab(numheads, numlegs):
    return (numlegs - 2 * numheads) / 2
chickens = numheads - findRab(numheads, numlegs)

print(chickens, findRab(numheads, numlegs))