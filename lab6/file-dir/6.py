'''Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt'''

k = 65

for i in range(65, 91):
    with open(chr(k)+'.txt', 'w') as f:
        f.writelines('')
    k += 1    
