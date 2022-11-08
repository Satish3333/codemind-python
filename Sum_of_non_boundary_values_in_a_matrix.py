a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for i in range(len(l1)):
    if i==0 or i==len(l1)-1:
        continue
    else:
        l1[i].pop(0)
        l1[i].pop(-1)
        s+=sum(l1[i])
print(s)