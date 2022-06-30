s=input()
b=[]
for i in s:
    p=int(i)
    if p%2!=0:
        b+=[p*p]
for j in b:
    print(j,end='')