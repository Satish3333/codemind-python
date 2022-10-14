n=input()
a=input()
c=0
l=[]
for i in n:
    if i==a:
        c+=1
        l.append(c)
if len(l)==0:
    print(-1)
else:
    print(l[-1])