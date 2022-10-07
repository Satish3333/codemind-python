n,m=map(int,(input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
for i in l1:
    if i in l2:
        l3.append(i)
for j in l3:
    if j not in l4:
        l4.append(j)
print(*l4) 