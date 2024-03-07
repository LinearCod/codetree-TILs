n = int(input())

cnt = n + 2

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(j + n*3*(i//2) + 1, end=' ')
            if i != 0 and j == n - 1:
                cnt = j + n*3*(i//2) + 1 + 2
        else:
            print(cnt + 2*j, end=' ')
    print()