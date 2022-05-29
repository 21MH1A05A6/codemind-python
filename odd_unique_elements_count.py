n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if(i%2!=0 and i not in b):
        c+=1
        b+=[i]
print(c)