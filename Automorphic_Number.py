n=int(input())
s=n**2
a=len(str(s))-len(str(n))
t=str(s)
b=t[a:]
if b==str(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")