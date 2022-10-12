n=input().split()
l=[]
for i in n:
    a=min(i)
    b=max(i)
    l.append(abs(ord(a)-ord(b)))
print(*l)