n=input().split()
a="aeiouAEIOU"
c=0
for i in n:
    if i[0] in a:
        c+=1
print(c)