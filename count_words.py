s=input()
n=s.split()
c=0
p='AEIOUaeiou'
for i in n:
    m=str(i)
    for j in range(len(m)):
        if m[0] in p and m[len(m)-1] not in p:
            c+=1
            break
print(c)
        