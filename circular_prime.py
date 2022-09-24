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
t=a
s=0
while a>0:
    r=a%10
    a=a//10
    s=s*10+r
if prime(t) and prime(s):
    print("circular prime")
elif prime(t):
    print("prime but not a circular prime")
else:
    print("not prime")
    
    
