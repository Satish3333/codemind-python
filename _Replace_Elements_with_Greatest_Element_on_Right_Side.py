n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)-1):
    a=l[i+1:]
    k.append(max(a))
k.append(-1)
print(*k)