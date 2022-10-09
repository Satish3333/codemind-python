n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
s=[]
for i in range (len(l)):
    if i%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
for i in range(len(l1)):
    for j in range(l1[i]):
        s.append(l2[i])
print(*s)
    