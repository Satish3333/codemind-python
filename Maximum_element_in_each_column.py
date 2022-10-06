a,b=map(int,input().split())
m=[]
for i in range(b):
    l=list(map(int,input().split()))
    m.append(l)
for j in range(len(m)):
    t=[]
    for k in range(len(m)):
        t.append(m[k][j])
    print(max(t))
    