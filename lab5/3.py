#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

s = input()

res = re.search(r'[a-z]+_([a-z]*)?', s)

if res:
    print(res.group())