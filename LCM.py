a,b=map(int,input().split())
if a>b:
    a,b=b,a
s=b
p=1
while True:
    if s%a==0:
        print(s)
        break
    else:
        s=b*p
    p+=1