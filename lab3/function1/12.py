'''Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******'''

nums = input().split()

def histogram(nums):
    for i in nums:
        print('*'* int(i))

histogram(nums)