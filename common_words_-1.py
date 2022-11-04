n=input().lower()
n1=n.split()
m=input().lower()
m1=m.split()
c=0
for i in m1:
    if m1.count(i)==1 and i in n1 and n1.count(i)==1 and i!=" ":
        c+=1
print(c)