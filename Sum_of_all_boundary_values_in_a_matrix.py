a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for i in range(len(l1)):
    if i==0 or i==len(l1)-1:
        s+=sum(l1[i])
    else:
        x=l1[i]
        y=x[0]
        z=x[-1]
        s+=z
        s+=y
print(s)
        
        
