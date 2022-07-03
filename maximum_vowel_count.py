s1=input()
s=s1.split()
c=0
a=[]
for i in s:
    n=str(i)
    for j in n:
        if j in 'aeiouAEIOU':
            c+=1
    a+=[c]
    c=0
print(max(a))