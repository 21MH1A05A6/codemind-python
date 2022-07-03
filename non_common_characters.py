n=input()
m=input()
s1=n.lower()
s2=m.lower()
b=[]
for i in s1:
    if i not in s2 and i not in b and i!=' ':
        b+=[i]
for k in s2:
    if k not in s1 and k not in b:
        b+=[k]
c=sorted(b)
for j in c:
    print(j,end='')