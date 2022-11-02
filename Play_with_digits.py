def dig(n):
    s=0
    while n>0:
        r=n%10
        n=n//10
        s=s+r
    return s
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    a=dig(i)
    k.append(a)
print(sum(k))