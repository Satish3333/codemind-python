a=int(input())
l=list(map(int,input().split()))
b=int(input())
for i in range(len(l)):
    if b in l:
        if b==l[i]:
            print(i)
    else:
        print(-1)
        break
        