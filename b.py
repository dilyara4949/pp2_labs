a, d = input(), 0
for i in range(len(a)):
    d += ord(a[i])
print('Oh, no!' if d <= 300 else 'It is tasty!')