n=input()
a=n.lower()
l=set(a)
c=0
for i in l:
    if i!=" ":
        c+=1
print(c)