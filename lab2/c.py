n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0:
            print(j, end=' ')    # 1st row
        elif j == 0:
            print(i, end=' ')    # 1st column
        elif i == j:
            print(i*i, end=' ')  # diagonal
        else:
            print(0, end=' ')
    print()






    