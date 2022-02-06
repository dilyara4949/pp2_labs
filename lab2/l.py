
a = input()
st = []
f = True
for i in a:
    if len(st) == 0 and (i == ')' or i == '}' or i == ']'):
        print('No')
        f = False
        break
    if i == '{' or i == '[' or i == '(':
        st.append(i)
    if i ==')' and st[-1]=='(':
        st.pop()
    if i =='}' and st[-1]=='{':
        st.pop()  
    if i ==']' and st[-1]=='[':
        st.pop()
    # if i ==')' and (st[-1]!='(' or i ==']') and (st[-1]!='[' or i=='}') and st[-1] != '{':
    #     print("No")
    #     break
    
if len(st) == 0 and f:
    print('Yes')
elif f and len(st) != 0:
    print('No')



