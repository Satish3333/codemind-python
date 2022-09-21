n=input()
a="aeiou"
c=0
l=[]
for i in n:
    if i in a:
        if i not in l:
            l.append(i)
if len(l)==5:
    print(True)
else:
    print(False)
