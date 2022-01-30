s = input()
def to_lowercase(s):
    ans = ''
    for i in range(len(s)):
        if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
            ans += chr(ord(s[i])+32)
        else:
           ans += s[i]
    print(ans)   
    
to_lowercase(s)