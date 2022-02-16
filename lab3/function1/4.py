myList = input().split()

def isPrime(num):    # check element of list, prime or not
    cnt = 0 
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            cnt += 1
    if cnt == 0 and num > 1:
        return True
    else:
        return False

primeNums = list(filter(lambda x : isPrime(int(x)), myList))
print(primeNums)