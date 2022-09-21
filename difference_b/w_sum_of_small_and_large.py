n=input().split()
l=[]
l1=[]
for i in n:
    a=list(i)
    a.sort()
    l.append(a[0])
    l1.append(a[-1])
c=0
e=0
for j in l:
    b=ord(j)
    c=c+b
for k in l1:
    d=ord(k)
    e=e+d
print(e-c)
    
