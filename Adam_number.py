n=int(input())
s=n*n
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
q=rev*rev
re=0
while(q):
    d=q%10
    re=re*10+d
    q=q//10
if(s==re):
    print('True')
else:
    print('False')