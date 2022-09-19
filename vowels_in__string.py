n=input()
a="AEIOUaeiou"
l=[]
for i in n:
    if i in a and i not in l:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*l)