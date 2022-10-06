n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    s=l1+l2
    s.sort()
    print(*s)