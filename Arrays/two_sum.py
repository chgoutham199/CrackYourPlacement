d=defaultdict()
for i,value in enumerate(a):
    d[value]=i
for i in range(len(a)):
    diff=k-a[i]
    if diff in d and d[diff]!=i:
            return [i,d[diff]]