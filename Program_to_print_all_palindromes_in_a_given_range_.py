a=int(input())
b=int(input())
for i in range(a,b+1):
    p=str(i)
    if(p==p[: :-1]):
        print(i,end=' ')