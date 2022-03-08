#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

s = input()

res = re.search(r'[A-Z][a-z]+', s)

if res:
    print(res.group())