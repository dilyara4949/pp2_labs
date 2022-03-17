# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = '/Users/dilaramuhambetova/pp2_labs/lab6'

for i in os.listdir(path):     # only directories
    if os.path.isdir(os.path.join(path, i)): print(i, end='   ')
print()
for i in os.listdir(path):      # only files
    if not os.path.isdir(os.path.join(path, i)): print(i, end= '    ')
print()

print(os.listdir(path))  # all directories, files

