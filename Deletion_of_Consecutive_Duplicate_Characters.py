t=int(input())
a=''
for i in range(t):
    s=input()
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            a+=s[i]
    print(len(s)-len(a)-1)
    a=''