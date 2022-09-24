n=int(input())
#s=int(pow(n,0.5))
c=0
for i in range(n+1):
    for j in range(i+1,n+1):
        a=j**2
        b=i**2
        if a+b==n:
            c+=1
            break
if c==0:
    print(False)
else:
    print(True)
