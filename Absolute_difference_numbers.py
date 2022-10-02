a,b=map(int,input().split())
a1=str(a)
a2=a1[::-1]
c1=a2[:b]
c2=a1[:b]
c3=c1[::-1]
print(abs(int(c2)-int(c3)))