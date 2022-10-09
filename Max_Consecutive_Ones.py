n=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in l:
    if i==1:
        c+=1
        if c>c1:
            c1=c
    else:
        c=0
print(c1)