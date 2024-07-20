m,diff=float('-inf'),0
for i in range(len(a)):
    if a[i]<m:
        m=a[i]
    else :
        diff=max(diff,a[i]-m)
return diff 
    
