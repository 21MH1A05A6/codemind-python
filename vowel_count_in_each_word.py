s1=input()
s=s1.split()
c=0
for i in s:
    n=str(i)
    for j in n:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')
    c=0