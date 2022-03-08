#Write a Python program to convert a given camel case string to snake case.

import re

camel = input() #camelCase


need = re.search(r'[A-Z]', camel)
while need:
    camel = re.sub(need.group(), '_'+chr(ord(need[0])+32), camel)
    need = re.search(r'[A-Z]', camel)
print(camel)  #snake