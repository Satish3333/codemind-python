n=int(input())
for i in range(n):
    m=input()
    a=m[::-1]
    if len(m)%2==0 and a==m:
        print("YES","EVEN")
    elif len(m)%2==1 and a==m:
        print("YES","ODD")
    else:
        print("NO")