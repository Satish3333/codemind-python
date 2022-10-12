n=input().split()
l=[]
for i in n:
    a=min(i)
    b=max(i)
    l.append(a)
    l.append(b)
print(*l)