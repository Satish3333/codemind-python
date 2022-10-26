def prime(d):
    c=[0]*(d+1)
    c[0]=1
    if d>=1:
        c[1]=1
    if d>=2:
        c[2]=2
    for i in range(3,d+1):
        c[i]=c[i-1]+c[i-2]+c[i-3]
    return c[d]
d=int(input())
print(prime(d))