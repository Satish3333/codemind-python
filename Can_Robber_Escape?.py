n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]>=n:
        print("NO")
        break
else:
    print("YES")