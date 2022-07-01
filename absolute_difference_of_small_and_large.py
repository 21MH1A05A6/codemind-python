s=input()
n=s.split()
for i in n:
    p=max(i)
    q=min(i)
    print(abs(ord(p)-ord(q)),end=' ')