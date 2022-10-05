import math 
n=int(input())
m=n
s=0
while n>0:
    r=n%10
    n=n//10
    a=math.factorial(r)
    s=s+a
if m==s:
    print("The number {} is a strong number".format(m))
else:
    print("The number {} is not a strong number".format(m))