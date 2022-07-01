s=input()
n=sorted(s)
for i in n:
    if i!=' ':
        print(i,n.count(i),end=' ')
        break
print(max(s),s.count(max(s)))