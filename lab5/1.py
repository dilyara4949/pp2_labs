#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

s = input()

need = r'a(b*)'
res = re.search(need, s)

if res:
    print(res.group())