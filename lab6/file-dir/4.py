'''Write a Python program to count the number of lines in a text file.'''

with open('/Users/dilaramuhambetova/pp2_labs/lab6/test.txt', 'r') as f:
    k = f.read().split('\n')
    print(len(k))
