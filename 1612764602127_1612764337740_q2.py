s="EduCatiON"
l,u=0,0
for i in s:
    if (i>='a'and i<='z'):
        l=l+1
    if(i>='A'and i<='Z'):
        u=u+1
print("small alphabets:",l)
print("capital alphabets:",u)

print(s.swapcase())



'''
list1=list(s)
new=[]
for i in list1:
    if i.isupper():
        i=""+i.lower()
    new.append(i)
    else:
        i=''+i.upper()
new.append(i)
print(''.join(new))
'''