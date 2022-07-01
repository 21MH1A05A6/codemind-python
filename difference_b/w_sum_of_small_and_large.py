s=input()
n=s.split()
ma,mi=0,0
for i in n:
    p=max(i)
    ma+=ord(p)
for j in n:
    q=min(j)
    mi+=ord(q)
print(ma-mi)