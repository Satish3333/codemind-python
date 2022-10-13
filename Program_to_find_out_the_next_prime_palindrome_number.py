from math import sqrt
def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def pali(n):
    n=str(n)
    s=n
    s=s[::-1]
    if s==n:
        return True
    return False
b=int(input())
i=b+1
while True:
    if prime(i) and pali(i):
        print(i)
        break
    else:
        i+=1