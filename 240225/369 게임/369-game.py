n = int(input())
for i in range(1,n+1):
    if i < 10:
        if i % 3 == 0:
            print(0, end=' ')
        else:
            print(i, end=' ')
    if i >= 10 and i % 2 == 0:
        if str(i)[0] == '3' or str(i)[1] == '3':
            print('0', end=' ')
        else:
            print(i, end=' ')
    elif i >= 10 and i % 2 != 0:
        if str(i)[0] == '3' or str(i)[1] == '3':
            print('0', end=' ')