n=input()
a=n.lower()
a1=set(a)
m=input()
b=m.lower()
b1=set(b)
l=[]
for i in b1:
    if i not in a1 and i!=" " and i not in l:
        l.append(i)
for j in a1:
    if j not in b1 and j!=" " and j not in l:
        l.append(j)
print(len(l))