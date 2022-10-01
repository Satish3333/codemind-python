m=int(input())
n=str(m)
t=n
a=1
s=0
for i in n:
    b=int(i)**a
    a+=1
    s=s+b
if s==m:
    print(True)
else:
    print(False)