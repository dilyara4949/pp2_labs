#Write a python program to convert snake case string to camel case string.

import re

snake = input()  # snake_case

while '_' in snake:
    need = r'_[a-z]'
    pos = re.search(need, snake)
    snake = re.sub(pos.group(), chr(ord(pos.group()[1])-32) ,snake)
print(snake) #camel




