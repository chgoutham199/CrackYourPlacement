c=0
for i in range(len(a)):
    a[c]=a[i]
    if a[i]!=0:
        c+=1
while(c<len(a)):
    a[c]=0
    c+=1