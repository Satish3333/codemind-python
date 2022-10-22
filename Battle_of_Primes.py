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
b=int(input())
d=1
c=a+b
while True:
    e=c+d
    if prime(e):
        print(d)
        break
    else:
        d+=1
        