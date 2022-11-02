n=input()
l=[]
n1=n.lower()
a1=list(n1.split(" "))
n2=n.upper()
a2=list(n2.split(" "))
s=list(a1[-1])
s.sort()
t=list(a2[-1])
t.sort()
if s[0] in n:
    l.append(s[0])
if t[0] in n:
    l.append(t[0])
print(l[0])
