n=input().lower()
l=list(n)
a=set(l)
m=input().lower()
l1=list(m)
b=set(l1)
s=[]
for i in a:
    if i  in b and i!=" ":
        s.append(i)
s.sort()
k=""
if len(s)==0:
    print(-1)
else:
    for j in s:
        k+=j
    print(k)
