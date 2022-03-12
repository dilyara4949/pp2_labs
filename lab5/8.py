#Write a Python program to split a string at uppercase letters.

import re

s = input()

s = re.split(r'[A-Z]+', s)

while '' in s:
    s.remove('')

print(s)