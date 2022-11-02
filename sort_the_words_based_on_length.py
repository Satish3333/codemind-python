n=input()
l=list(n.split())
l.sort()
for i in range(len(l)):
   for j in range(i,len(l)):
       if len(l[i])>len(l[j]):
           l[i],l[j]=l[j],l[i]
print(*l)
       