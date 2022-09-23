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
c=0
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            continue
        else:
            c+=1
print(c)

