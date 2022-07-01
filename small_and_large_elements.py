s=input()
n=s.split()
if len(n)>1:
    for i in range(len(n)-1):
        print(min(n[0]),max(n[len(n)-1]))
        break
else:
    print(min(s),max(s))