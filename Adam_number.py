def rev(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    return s
a=int(input())
b=rev(a)
c=a**2
d=b**2
if c==rev(d):
    print(True)
else:
    print(False)
