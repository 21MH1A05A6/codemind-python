t=int(input())
b=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(1,n+1):
        b+=[j]
    for k in b:
        if k not in a:
            print(k)
            break