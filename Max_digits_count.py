n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    x=str(i)
    p=len(x)
    b+=[p]
for j in b:
    q=max(b)
    print(b.count(q))
    break