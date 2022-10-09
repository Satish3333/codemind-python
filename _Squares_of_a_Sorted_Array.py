n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    a=i*i
    k.append(a)
    k.sort()
print(*k)