def rev(n):
    a=str(n)
    b=a[::-1]
    return n+int(b)
n=int(input())
while True:
    s=rev(n)
    a=str(s)
    b=a[::-1]
    if b==a:
        print(a)
        break
    else:
        n=int(a)