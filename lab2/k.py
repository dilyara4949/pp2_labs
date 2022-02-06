import re
a = input()
a = re.split('[,.{" "}?!-]', a)
while '' in a: a.remove('')
a.sort()
d = dict({})
for i in a:
    d[i] = 0
print(len(d))

for i in d:
    print(i)