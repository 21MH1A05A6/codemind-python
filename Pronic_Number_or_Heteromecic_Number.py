n=int(input())
x=1
c=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        c+=1
        break
if(c==1):
    print('YES')
else:
    print('NO')