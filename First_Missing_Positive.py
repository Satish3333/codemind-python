n=int(input())
l=list(map(int,input().split()))
a=1
while True:
    if a not in l:
        print(a)
        break
    else:
        a+=1