n=int(input())
a=list(map(int,input().split()))
b=[]
s=[]
for i in a:
    x=str(i)
    p=len(x)
    s+=[p]
c=max(s)
for i in a:
    x=str(i)
    p=len(x)
    if(p==c):
        print(i,end=' ')