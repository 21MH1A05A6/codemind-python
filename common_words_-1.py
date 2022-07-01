s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
n=s3.split()
m=s4.split()
b=[]
c=0
for i in n:
    if i in m and i not in b:
        b+=[i]
        c+=1
for j in m:
    if j in n and j not in b:
        b+=[j]
        c+=1
print(c)