a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for i in range(a):
    for j in range(b):
        if i==j or i+j==a-1:
            s=s+l1[i][j]
print(s)
        