n=int(input())
l=list(map(int,input().split()))
b=l[::-1]
b.sort()
b=b[::-1]
if b==l:
    print("yes")
else:
    print("no")