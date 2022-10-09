n=int(input())
l=list(map(int,input().split()))
k=[]
k1=[]
for i in l:
    if i not in k:
        k.append(i)
    else:
        k1.append(i)
l1=[]
for i in k:
    if i not in k1:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    print(max(l1))