n=int(input())
s=str(n)
c,d=0,0
for i in s:
    if int(i)%2==0:
        c+=1
    elif int(i)%2!=0:
        d+=1
if(c==len(s)):
    print('Even')
elif(d==len(s)):
    print('Odd')
else:
    print('Mixed')