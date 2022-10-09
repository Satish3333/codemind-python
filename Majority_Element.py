n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l.count(l[i])>c:
        c=l.count(l[i])
        t=l[i]
print(t)