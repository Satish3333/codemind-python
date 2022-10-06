a=int(input())
b=list(map(int,input().split()))
c=0
c1=0
for i in b:
    if i%2==0:
        c+=1
    else:
        c1+=1
print(c,c1)