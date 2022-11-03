n=input()
n1=n.lower()
n2=n1.split()
m=input()
m1=m.lower()
m2=m1.split()
for i in m2:
    if i in n2 :
        print(i,end=" ")
