def pali(n):
    s=0
    a=n
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    if s==a:
        return True
    else:
        return False
b=int(input())
l1=0
l2=0
for i in range(b-1,1,-1):
    if pali(i):
        l1=i
        break
for j in range(b+1,100000):
    if pali(j):
        l2=j
        break

d1=b-l1
d2=l2-b
if d1==d2:
    print(l1,l2)
elif d1>=d2:
    print(l2)
else:
    print(l1)
