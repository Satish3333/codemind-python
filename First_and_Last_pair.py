def fun(k):
    l1=[]
    s=len(k)-1
    for i in range(len(k)//2):
        l1.append(k[i])
        l1.append(k[s])
        s=s-1
    return l1
n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
if n%2==1:
    a=l[:(len(l)//2)+1]
    b=l[(len(l)//2)+1:]
    b.insert(0,0)
    l2=[]
    l2=a+b
    print(*fun(l2))
else:
    print(*fun(l))
    