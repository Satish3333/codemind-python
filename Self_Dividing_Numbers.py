def fun(n):
    s=0
    a=n
    k=0
    while n>0:
        r=n%10
        n=n//10
        k+=1
        if r!=0 and a%r==0:
            s+=1
    if s==k:
        return True
    return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if fun(i):
        print(i,end=" ")
