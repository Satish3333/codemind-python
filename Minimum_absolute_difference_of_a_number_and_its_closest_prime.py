def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a=int(input())
l1=0
l2=0
for i in range(a,1,-1):
    if prime(i):
        l1=i
        break
for j in range(a,1000):
    if prime(j):
        l2=j
        break
d1=l2-a
d2=a-l1
print(min(d1,d2))
    