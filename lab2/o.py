a, b = map(str, input().split('+'))

myDict = {
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOU' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SEV' : 7,
    'EIG' : 8,
    'NIN' : 9,
    'ZER' : 0
}
def get_key(val):
    for key, value in myDict.items():
         if val == value:
             return key

k, ans = 1, 0
for i in range(len(a), 0, -3):   # convert a
    ans += myDict[a[i-3: i]] * k
    k *= 10
k = 1
for i in range(len(b), 0, -3):   # convert b and get sum
    ans += myDict[b[i-3: i]] * k
    k *= 10

j = len(str(ans))
for i in range(j-1, -1, -1):
    print(get_key((ans // (10**i))%10), end='')
