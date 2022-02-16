'''Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False'''

mylist = input().split()

def spy_game(mylist):
    strMylist = ''
    for i in mylist:
        if i == '0' or i == '7':       # [1,2,4,0,0,7,5] ---> '007',   [1,7,2,0,4,5,0] ---> '700'
            strMylist += i
    if '007' in strMylist:
        print(True)
    else:
        print(False)

spy_game(mylist)
