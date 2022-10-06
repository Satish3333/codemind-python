n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    for j in range(1,a+1):
        if j not in l:
            print(j)