a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
c=0
for i in range(len(l1)):
    for j in range(b):
        if l1[i][j]%2==0:
            s+=l1[i][j]
        else:
            c+=l1[i][j]
print(s,c)
    