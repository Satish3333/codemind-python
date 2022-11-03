def fun(l,k):
    l1=[]
    for i in range(len(l)):
        l1.append(l[i])
        l1.append(k[i])
    return l1
n=int(input())
k=list(map(int,input().split()))
e=[]
o=[]
for i in k:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)<len(o):
    for j in range(len(o)-len(e)):
        e.append("#")
else:
    for j in range(len(e)-len(o)):
        o.append("#")
l1=fun(e,o)
l2=[]
for i in l1:
    if i!="#":
        l2.append(i)
if n%2==1:
    l2.append(0)
    print(*l2)
else:
    print(*l2)