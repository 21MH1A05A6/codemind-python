n=int(input())
for i in range(n):
    s=input()
    for i in s:
        if i not in '1234567890':
            print('False')
            break
    else:
        print('True')