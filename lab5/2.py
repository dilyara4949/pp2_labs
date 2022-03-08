#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

s = input()

need = r'a(bbb|bb)'
res = re.search(need, s)

if res:
    print(res.group())