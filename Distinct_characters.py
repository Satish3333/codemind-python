n=input()
a=n.lower()
l=list(n.split())
l1=[]
for i in a:
    if n.count(i)==1:
        l1.append(i)
l1.sort()
c=""
for i in l1:
    if i!=' ':
        c+=i
print(c)