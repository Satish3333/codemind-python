n=int(input())
k=list(map(str,input().split()))
l=[]
for i in  k:
    a=len(i)
    l.append(a)
s=max(l)
for j in k:
    if len(j)==s:
        print(j,end=" ")