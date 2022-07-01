s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
n=s3.split()
m=s4.split()
b,d=[],[]
c=0
for i in n:
    if i in m:
        b+=[i]
for j in m:
    if j in n:
        b+=[j]
for k in b:
    if b.count(k)==2 and k not in d:
        d+=[k]
        c+=1
print(c)