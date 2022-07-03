s1=input()
s=s1.split()
a=[]
for i in range(len(s)):
    p=s[i]
    if i%2==0:
        a+=[p[::-1]]
    else:
        a+=[p]
for k in a:
    print(k,end=' ')