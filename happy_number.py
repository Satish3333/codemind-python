def fun(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        a=r**2
        s=s+a
    return s
t=int(input())
while True:
    if t<=10:
        if t==1 or t==7 or t==10:
            print(True)
            break
        else:
            print(False)
            break
    else:
        t=fun(t)