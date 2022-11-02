def fun(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>=l[j]:
                return False
    return 1
n=int(input())
l=list(map(int,input().split()))
if fun(l):
    print('yes')
else:
    print('no')