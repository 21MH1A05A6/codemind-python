s1=input()
s2=input()
n=s1.lower()
m=s2.lower()
p=[]
for i in n:
    if i not in m and i not in p:
        p+=[i]
for j in m:
    if j not in n and j not in p:
        p+=[j]
b=sorted(p)
for k in b:
    if k!=' ':
        print(k,end='')