n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
for i in range(len(l)):
    a=l[i]+l1[i]
    print(a,end=" ")