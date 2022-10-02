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
b=a
l=[]
while a>0:
    r=a%10
    a=a//10
    l.append(r)
for i in l:
    continue
if prime(i) and prime(b):
    print("Mega Prime")
else:
    print("Not Mega Prime")
