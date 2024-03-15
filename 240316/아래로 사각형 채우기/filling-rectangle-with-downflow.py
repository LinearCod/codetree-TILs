n = int(input())

arr_2d = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(n): 
    for j in range(n):
        arr_2d[i][j] += n * j + i
    
for i in arr_2d:
    for j in i:
        print(j, end=' ')
    print()