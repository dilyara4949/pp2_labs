'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''

nums = input().split()       # 1 2 3 4 5 6 7

def has_33(nums):
    strNums = ''
    for i in range(len(nums)):
        strNums += nums[i]    # 1234567
    if '33' in strNums:
        print(True)
    else:
        print(False)

has_33(nums)