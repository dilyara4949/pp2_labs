bin = int(input())

# def convert(bin):
#     return int(bin, 2)
# print(convert(bin))
def to_dec(bin, j):     # j - степень
    if bin == 1 or bin == 0:
        return bin * (2 ** j)
    last = bin % 10
    return  last * (2 ** j) + to_dec(bin//10, j+1)
print(to_dec(bin, 0))
