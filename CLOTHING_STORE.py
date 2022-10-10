n=int(input())
l=list(map(int,input().split()))
a=set(l)
k=[]
c=0
for i in a:
    k.append(l.count(i))
for j in k:
    c+=j//2
print(c)