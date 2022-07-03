s1=input()
s=s1.split()
c,co,d=0,0,0
a=[]
for i in s:
    n=str(i)
    for j in n:
        if j in 'aeiouAEIOU':
            c+=1
    a+=[c]
    c=0
for k in s:
    m=str(k)
    for l in m:
        if l in 'aeiouAEIOU':
            co+=1
    if(co==min(a)):
        d+=1
    co=0
print(d)