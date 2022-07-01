s=input()
n=s.split()
c=0
for i in n:
    p=str(i)
    for j in p:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')
    c=0