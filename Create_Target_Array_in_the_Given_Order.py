n=int(input())
l1=list(map(int,input().split()))
n1=int(input())
l2=list(map(int,input().split()))
k=[]
for i in range(n):
    k.insert(l2[i],l1[i])
print(*k)