s=input("Enter the string ,mixed capital and small letters")
l,u=0,0
for i in s:
    if (i>='a'and i<='z'):
        l=l+1
    if(i>='A'and i<='Z'):
        u=u+1
print("small alphabets:",l)
print("capital alphabets:",u)

print(s.swapcase())


