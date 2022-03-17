'''Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.'''

import os

path = '/Users/dilaramuhambetova/pp2_labs/lab6/file-dir/A.txt'

if os.path.exists(path):
    os.remove(path)
else: print('Path does not exist')