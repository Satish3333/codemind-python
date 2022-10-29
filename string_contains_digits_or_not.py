n=int(input())
for i in range(n):
    a=input()
    b="123456789"
    l=list(b)
    for j in a:
        if j in l:
            print("Yes")
            break
    else:
        print("No")