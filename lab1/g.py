bin = input()

# def convert(bin):
#     return int(bin, 2)
# print(convert(bin))

dec, n, j = 0, len(bin), 0
def to_dec(bin, dec, n, j):
    if n == j:
        return dec
    return  int(bin[n-1-j]) * (2 ** j) + to_dec(bin, dec, n, j+1)
print(to_dec(bin, dec, n, j))