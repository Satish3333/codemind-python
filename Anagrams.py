n=input().lower()
m=input().lower()
for i in m:
    if i not in n:
        print(False)
        break
else:
    print(True)