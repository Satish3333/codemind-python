n=input()
s=n.lower()
a=set(s)
l=[]
for i in a:
    if i!=" ":
        l.append(i)
l.sort()
b=""
for i in l:
    b+=i
print(b)