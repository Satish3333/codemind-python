def rev(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    return s
a=int(input())
t=rev(a)
u=t**2
v=a**2
if v==rev(u):
    print(True)
else:
    print(False)

