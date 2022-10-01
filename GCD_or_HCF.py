a,b=map(int,input().split())
if a>b or b>a:
    a,b=b,a
l=[]
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        l.append(i)
print(max(l))