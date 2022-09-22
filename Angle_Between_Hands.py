a,b=map(int,input().split(":"))
c=30*a-11/2*b
if c<0:
    c=c*-1
t=c
k=abs(t-360)
if t<k:
    print(t)
else:
    print(k)
