a,b = map(int, input().split())

if b - 2 != a:
    lit = []
    for i in range(b, a-1, -2):
        lit.append(i)
    for i in range(1, 10):
        for j in lit:
            print(f'{j} * {i} = {j*i}', end=' ')
            if j > len(lit) - 1 and b != a:
                print('/', end=' ')
        print()
else:
    for i in range(1, 10):
        for j in range(b, a-1, -2):
            print(f'{j} * {i} = {j*i}', end=' ')
            if j != a:
                print('/', end=' ')
        print()