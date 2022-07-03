n=input()
x=set(n.lower())
p=sorted(x)
for i in p:
    if i!=' ':
        print(i,end='')