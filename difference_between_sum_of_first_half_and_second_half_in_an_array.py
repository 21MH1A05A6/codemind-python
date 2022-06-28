n=int(input())
a=list(map(int,input().split()))
s1,s2=0,0
for i in range(0,n//2+1):
    s1+=i
for j in range(n//2+1,n+1):
    s2+=j
print(s2-s1)