n = int(input())

cnt = 0

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('* ', end='')
        elif i != 0 and  j <= cnt:
            print('* ', end='')
        else:
            print('  ', end='')
    if i >= 1:
        cnt += 1
    print()