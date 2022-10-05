def ds(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        a=r**2
        s=s+a
    return s
a=int(input())
while True:
    if a<10:
        if a==1 or a==7:
            print(True)
            break
        else:
            print(False)
            break
    else:
        a=ds(a)