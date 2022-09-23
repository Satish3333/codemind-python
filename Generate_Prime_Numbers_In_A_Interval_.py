def prime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i):
        print(i)