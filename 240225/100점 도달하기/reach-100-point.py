n = int(input())
for i in range(n,101):
    if 70 > i >= 60:
        print('D', end=' ')
    elif 80 > i >= 70:
        print('C', end=' ')
    elif 90 > i >= 80:
        print('B', end=' ')
    elif i >= 90:
        print('A', end=' ')
    else:
        print('F', end=' ')