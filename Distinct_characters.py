n=input()
x=list(n)
b=[]
for i in x:
    if  i in 'abcdefghijklmnopqrstuvwxyz' and x.count(i)==1:
        b+=[i]
p=sorted(b)
for j in p:
    print(j,end='')