n=input()
c=0
s=0
for i in n:
    if int(i)%2==0:
        c+=1
    elif int(i)%2==1:
        s+=1
    else:
        c+=1
if c==len(n):
    print("Even")
elif s==len(n):
    print("Odd")
else:
    print("Mixed")