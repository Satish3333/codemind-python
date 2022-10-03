n=int(input())
c=0
c1=0
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j==n:
            c=i
            c1=j
if c1-c==1:
    print("YES")
else:
    print("NO")
