def fun(l):
    a=l[::-1]
    a.sort()
    if a==l or l==a[::-1]:
        return True
    return False
a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
c=0
for i in l1:
    if fun(i):
        c+=1
print(c)