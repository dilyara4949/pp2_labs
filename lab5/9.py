#Write a Python program to insert spaces between words starting with capital letters.

import re

s = input()
s += ' '

need = re.search(r'[A-Z][a-z]*[A-Z]', s)

while need:
    newstr = need.group()
    last = newstr[len(newstr)-1] 
    newstr = newstr[:len(newstr)-1] + ' ' + last

    
    s = re.sub(need.group(), newstr, s)       # replacing 

    need = re.search(r'[A-Z][a-z]*[A-Z]', s)     # update new word with cap letter


print(s)
