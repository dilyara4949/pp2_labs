#Write a Python program to split a string at uppercase letters.

import re

s = input()

s = re.split('[A-Z]+', s)
print(s)