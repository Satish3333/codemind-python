l=int(input())
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a<l or b<l:
        print("UPLOAD ANOTHER")
    elif a==b :
        print("ACCEPTED")
    else:
        print("CROP IT")
