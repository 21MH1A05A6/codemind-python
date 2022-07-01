s1=input()
s2=input()
n=s1.lower()
m=s2.lower()
p=[]
c=0
for i in n:
    if i!=' ':
        if i in m and i not in p:
            p+=[i]
            c+=1
for j in m:
    if j!=' ':
        if j in n and j not in p:
            p+=[j]
            c+=1
print(c)