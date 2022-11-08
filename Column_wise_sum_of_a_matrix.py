a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
k=[]
for i in range(b):
    a=0
    for j in range(len(l1)):
        a=a+l1[j][i]
    k.append(a)
print(*k)
    