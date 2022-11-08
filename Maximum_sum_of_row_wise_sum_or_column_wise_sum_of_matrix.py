a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
k=[]
for i in l:
    k.append(sum(i))
for i in range(len(i)):
    s=0
    for j in range(len(l)):
        s=s+l[j][i]
        k.append(s)
print(max(k))
