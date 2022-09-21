def pali(n):
    s=0
    a=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if a==s:
        return True
    else:
        return False
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    if pali(i):
        l.append(i)
print(*l)
        
        