n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=[]
for i in range(len(l)):
    if a==l[i]:
        k.append(i)
if len(k)!=0:
    print(k[0],k[-1])
else:
    print("-1 -1")