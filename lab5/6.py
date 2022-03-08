#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

s = input()

res = re.sub('\s|\.|\,', ':', s)

print(res)