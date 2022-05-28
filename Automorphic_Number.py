n=int(input())
q=''
q+=str(n)
s=''
sq=n*n
s+=str(sq)
if(q in s):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')