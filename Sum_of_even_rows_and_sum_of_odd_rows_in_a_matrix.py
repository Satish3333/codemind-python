a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
es=0
os=0
for i in range(len(l1)):
    if i%2==0:
        es+=sum(l1[i])
    else:
        os+=sum(l1[i])
print(es,os)

        