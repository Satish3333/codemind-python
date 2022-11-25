n=int(input())
a=1
b=1
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(" ",end="")
    print(str(a)*b)
    a+=1
    b+=2