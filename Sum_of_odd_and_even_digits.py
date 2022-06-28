n=int(input())
a=list(map(int,input().split()))
b,c=0,0
for i in range(len(a)):
    if i%2!=0:
        b+=a[i]
    else:
        c+=a[i]
d=c-b
if(d==0):
    print('YES')
else:
    print('NO')