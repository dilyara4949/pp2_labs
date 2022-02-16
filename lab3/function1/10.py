'''Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.'''
nums = input().split()

def delRepetitions(nums):
    newNums = []
    for i in nums:
        if i not in newNums:
            newNums.append(i)
    print(newNums)

delRepetitions(nums)