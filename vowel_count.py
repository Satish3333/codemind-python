n=input()
a="AEIOUaeiou"
l=[]
for i in n:
    if i in a:
        l.append(i)
print(len(l))