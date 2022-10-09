n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    a=1
    if l[i]>=1:
        b=i
        for j in range(len(l)):
            if b==j:
                continue
            else:
                a=a*l[j]
        print(a,end=" ")
    else:
        print(l[i],end=" ")
        