n=input().split()
a="aeiou"
l=[]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    l.append(c)
print(l.count(min(l)))
        
            
