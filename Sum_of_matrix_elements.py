a=int(input())
b=int(input())
k=[]
for i in range(a):
    l=list(map(int,input().split()))
    k.append(l)
c=0
for j in k:
    a=sum(j)
    c=c+a
print(c)