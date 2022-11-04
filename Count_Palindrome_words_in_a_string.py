def fun(n):
    b=n.lower()
    a=list(n)
    s=a[::-1]
    if s==a:
        return True
    else:
        return False
n=input()
k=n.lower()
k1=k.split()
c=0
for i in k1:
    if fun(i):
        c+=1
print(c)