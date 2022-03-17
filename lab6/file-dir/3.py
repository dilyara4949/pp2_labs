'''Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path.'''

import os

path = '/Users/dilaramuhambetova/pp2_labs/lab6'

if os.path.exists(path):
    print('Exists')
    print('File name :', os.path.basename(path))
    print('Dir portion :', os.path.dirname(path))


else: print("Path doesn't exist")