n=input()
c=0
l=[]
for i in n:
    if i.isdigit():
        c+=1
        l.append(c)
if len(l)==0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(l[-1]))