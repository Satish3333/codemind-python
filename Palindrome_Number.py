n=int(input())
for i in range(n):
    a=int(input())
    c=0
    b=a
    while a>0:
        r=a%10
        c=c*10+r
        a=a//10
    if b==c:
        print(True)
    else:
        print(False)
    