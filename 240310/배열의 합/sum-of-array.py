array = []
for _ in range(4):
    array_1 = list(map(int, input().split()))
    array.append(array_1)

for i in range(4):
    print(sum(array[i]))