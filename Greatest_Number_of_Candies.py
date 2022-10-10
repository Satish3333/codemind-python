n=int(input())
l=list(map(int,input().split()))
a=int(input())
s=max(l)
for i in l:
    if a+i>=s:
        print(True,end=" ")
    else:
        print(False,end=" ")
    