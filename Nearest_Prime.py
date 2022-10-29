def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    a=int(input())
    s=0
    t=0
    for j in range(a,100+a):
        if prime(j):
            s=j
            break
    for k in range(a,0,-1):
        if prime(k):
            t=k
            break
    d1=a-t
    d2=s-a
    if d1<=d2:
        print(t)
    else:
        print(s)
        
        
            
            