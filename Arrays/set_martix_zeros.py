c=1
for i in range(len(a)) :
    for j in range(len(a[0])):
        if a[i][j]==0:
            a[i][0]=0
            if j!=0:
                a[0][j]=0
            else :
                c=0
for i in range(1,len(a)):
    for j in range(1,len(a[0])):
        if a[i][j]!=0 and a[i][0]==0 or a[0][j]==0:
            a[i][j]=0
if a[0][0]==0:
    for i in range(len(a[0])):
        a[0][i]=0
if c==0 :
    for i in range(len(a)):
        a[i][0]=0