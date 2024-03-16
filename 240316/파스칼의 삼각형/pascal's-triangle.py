n = int(input())

arr_2d = [
    [j // j for j in range(1, i + 1)]
    for i in range(1, n + 1)
]

for i in range(n):
    for j in range(i):
        if j == 0:
            continue
        else:
            arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]
    
for i in arr_2d:
    for j in i:
        print(j, end=' ')
    print()