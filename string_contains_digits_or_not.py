n=int(input())
for i in range(n):
    s=input()
    for i in s:
        if i in '1234567890':
            print('Yes')
            break
    else:
        print('No')
