n=int(input())
s=1
c=0
while n>0:
    r=n%10
    n=n//10
    s=s*r
    c=c+r
print(s-c)