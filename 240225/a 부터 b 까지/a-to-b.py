a,b = map(int, input().split())
for i in range(a,b+1):
    if i == a:
        print(i, end=' ')
    if i != a:
        i = c
    if i % 2 != 0:
        c = i * 2
        if c > b:
            pass
        else:
            print(c, end=' ')
    elif i % 2 == 0:
        c = i + 3
        if c > b:
            pass
        else:
            print(c, end=' ')