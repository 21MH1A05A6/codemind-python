n=int(input())
for p in range(0,10):
    if(p*(p+1)==n):
        print('YES')
        break
else:
    print('NO')