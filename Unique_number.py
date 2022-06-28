n=int(input())
m=str(n)
for i in m:
    p=m.count(i)
    if(p!=1):
        print('Not Unique Number')
        break
else:
    print('Unique Number')