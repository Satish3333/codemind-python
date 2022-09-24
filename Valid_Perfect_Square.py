def sqrt(n):
    s=n**0.5
    if n%s==0:
        return True
    else:
        return False
a=int(input())
for i in range(a):
    b=int(input())
    print(sqrt(b))