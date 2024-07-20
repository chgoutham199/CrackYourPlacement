j=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        a[j]=a[i+1]
        j+=1
return j