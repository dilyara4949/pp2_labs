'''Write a Python program to write a list to a file.'''
myList = [1, 2, 3, 4, 5, 6, 7]
myList = str(myList)
with open('test.txt', 'a') as f:
    f.write('\n')
    f.write(myList)