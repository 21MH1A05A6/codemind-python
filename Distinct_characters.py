n=input()
x=list(n)
s=''
for i in x:
    if  i in 'abcdefghijklmnopqrstuvwxyz' and x.count(i)==1:
        s+=i
p=sorted(s)
for j in p:
    print(j,end='')