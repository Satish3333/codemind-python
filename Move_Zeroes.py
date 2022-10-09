n=int(input())
l=list(map(int,input().split()))
s=[]
c=l.count(0)
for i in l:
    if i!=0:
        s.append(i)
for j in range(c):
    s.append(0)
print(*s)