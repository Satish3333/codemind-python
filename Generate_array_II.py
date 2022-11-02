n=int(input())
l=list(map(int,input().split()))
k1=[]
k2=[]
for i in range(len(l)):
    if i%2==0:
        k1.append(l[i])
    else:
        k2.append(l[i])
for i in range(len(k2)):
    for j in range(k2[i]):
        print(k1[i],end=" ")
        
        