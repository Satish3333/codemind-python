n=input()
l=list(n.split())
l1=[]
l3=list(n)
for i in range(len(l)):
    s=l[i]
    for j in range(len(s)):
        l1.append(ord(s[j]))
a=chr(min(l1))
ac=l3.count(a)
b=chr(max(l1))
bc=l3.count(b)
print(a,ac,b,bc)