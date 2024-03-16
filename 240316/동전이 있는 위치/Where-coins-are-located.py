n,m = map(int, input().split())

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r - 1][c - 1] = 1

for i in placed:
    for j in i:
        print(j, end=' ')
    print()