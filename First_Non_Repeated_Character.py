n=int(input())
for i in range(n):
    a=int(input())
    b=input()
    for j in b:
        if b.count(j)==1:
            print(j)
            break
    else:
        print(-1)