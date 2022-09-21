n=input()
a=input()
b='aeiou'
for i in range(len(n)):
    if a in n[i]:
        print(True)
        print(i)
        break
else:
    print(False)
        
        