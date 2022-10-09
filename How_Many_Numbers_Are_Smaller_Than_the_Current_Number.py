def fun(a,b):
    c=0
    for i in range(len(b)):
        if a>b[i]:
            c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    s.append(fun(l[i],l))
print(*s)
    