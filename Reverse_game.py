def rev(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    return s
a=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    a=rev(i)
    l1.append(a)
print(*l1)