def fib(n):
    a=0
    b=1
    l=[]
    l.append(a)
    l.append(b)
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
        l.append(c)
    if n in l:
        return True 
    else:
        return False
a=int(input())
l1=0
l2=0
for i in range(a,1000):
    if fib(i):
        l1=i
        break
for j in range(a,1,-1):
    if fib(j):
        l2=j
        break
d1=l1-a
d2=a-l2
if d1==d2:
    print(l2,l1)
elif d1>d2:
    print(l2)
else:
    print(l1)