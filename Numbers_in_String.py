n=input()
a="qazxswedcrfvtgbyhnujmikolp"
l1=0
for i in n:
    if i.isdigit():
        l1=l1+int(i)
print(l1)