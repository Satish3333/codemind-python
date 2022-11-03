n=input().lower()
l=list(n)
a=set(l)
m=input().lower()
l1=list(m)
b=set(l1)
s=[]
for i in a:
    if i not in b:
        s.append(i)
for j in b:
    if j not in a:
        s.append(j)
s.sort()
k=""
for i in s:
    if i!=" ":
        k+=i
print(k)
    
