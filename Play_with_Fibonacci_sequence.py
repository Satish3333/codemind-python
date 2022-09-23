n=int(input())
a=0
b=1
l=[]
l.append(a)
l.append(b)
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    l.append(c)
print(*l)