n=input()
a=n.lower()
l=list(a)
a=l[::-1]
if a==l:
    print(True)
else:
    print(False)