n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
x=[]
co=0
for i in a:
    if(i<b or i>c):
        if i not in x:
            co+=1
            x+=[i]
if(co==0):
    print('-1')
else:
    print(max(x))