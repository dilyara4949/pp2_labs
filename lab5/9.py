#Write a Python program to insert spaces between words starting with capital letters.

import re

s = input()
s += ' '

need = re.search(r'[A-Z][a-z]+', s)

while need:
    repl = re.sub('', ' ', need.group())    # inserting spaces between word
    repl = repl.strip()
    s = re.sub(need.group(), repl, s)       # replacing 

    need = re.search(r'[A-Z][a-z]+', s)     # update new word with cap letter


print(s)