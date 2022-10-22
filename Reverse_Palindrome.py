def rev(n):
    a=str(n)
    s=a[::-1]
    return n+int(s)
n=int(input())
while True:
    b=rev(n)    
    s=str(b)
    a=s[::-1]
    if a==s:
        print(a)
        break
    else:
        n=int(a)