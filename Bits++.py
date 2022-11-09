n=int(input())
r=0
for i in range(n):
    j=input()
    if j=="++X" or j=="X++":
        r+=1
    elif j=="--X" or j=="X--":
        r-=1
print(r)