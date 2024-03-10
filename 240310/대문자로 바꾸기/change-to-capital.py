array = []
for _ in range(5):
    array_1 = list(map(str, input().split()))
    array.append(array_1)

for i in range(5):
    for j in range(3):
        print(array[i][j].upper(), end=' ')
    print()