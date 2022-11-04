n=input()
m=input()
n1=n.lower()
m1=m.lower()
n2=n1.split()
m2=m1.split()
l=[]
for i in m2:
    if m2.count(i)==1 and i in n2 and n2.count(i)==1:
        l.append(i)
print(len(l))