#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

s = input()

res = re.search(r'a..b', s)

if res: print(res.group())