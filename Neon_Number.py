n=int(input())
s=str(n*n)
l=[]
for i in s:
    l.append(int(i))
b=sum(l)
if b==n:
    print("Neon Number")
else:
    print("Not Neon Number")