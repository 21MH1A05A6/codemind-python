n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    s=len(str(i))
    if s%2==0:
        c+=1
print(c)