def fun(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+i
    return s
l=list(map(int,input().split(",")))
l1=[]
for i in l:
    t=fun(i)
    if t in l:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    l1.sort()
    print(*l1)