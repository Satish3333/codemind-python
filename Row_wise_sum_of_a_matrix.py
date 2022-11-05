a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
k=[]
for i in range(len(l1)):
    a=sum(l1[i])
    k.append(a)
print(*k)


    