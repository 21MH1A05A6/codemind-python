s=input()
n=s.lower()
k=n.split()
c=0
b=[]
for i in n:
    if n.count(i)>=len(k) and i not in b:
        b+=[i]
        c+=1
b1=sorted(b)
if c==0:
    print('-1')
else:
    for j in b1:
        print(j)
        break