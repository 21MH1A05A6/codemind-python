s=input()
m=(s.lower()).split()
for i in m:
    n=str(i)
    if n==n[::-1]:
        print('True')
    else:
        print('False')