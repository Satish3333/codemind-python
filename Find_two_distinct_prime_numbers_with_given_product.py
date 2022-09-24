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
x=0
y=0
for i in range(1,a+1):
    for j in range(i,a+1):
        if prime(i) and i*j==a:
            x=i
            y=j
if x==0 and y==0:
    print(-1)
else:
    print(x,y)