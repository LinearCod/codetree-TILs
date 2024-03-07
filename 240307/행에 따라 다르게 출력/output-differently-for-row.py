n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(j + n*3*(i//2) + 1, end=' ')
        else:
            if i != 1:
                print(n + 2 + n*i + 2*j, end=' ')
            else:
                print(n + 2 + 2*j, end=' ')
    print()