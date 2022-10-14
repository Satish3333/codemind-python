n1=input()
n=n1.lower()
m="aeiou"
k="bcdfghjklmnpqrstvwxyz"
c=0
c1=0
c2=0
c3=0
l=[]
for i in n:
    if i in m:
        c+=1
    if i.isdigit():
        c1+=1
    if i in k:
        c2+=1
    if i==" ":
        c3+=1
print("Vowels:",c)
print("Consonants:",c2)
print("Digits:",c1)
print("White spaces:",c3)  
