S=input()
s=0
for i in S:
    if i in '123456789':
        s+=int(i)
print(s)