a.sort()
c=float('inf')
j=m-1
i=0
while(j<len(a)):
    c=min(c,a[j]-a[i])
    i+=1
    j+=1
return c