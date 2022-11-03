n=input().lower()
n1=set(n)
m=input().lower()
m1=set(m)
l=[]
for i in m1:
    if i in n1 and i!=" " and i not in l:
        l.append(i)
for j in n1:
    if j in m1 and j!=" " and j not in l:
        l.append(j)
print(len(l))