array = []
sum_array = 0
avg_array = 0

for _ in range(2):
    array_1 = list(map(int, input().split()))
    array.append(array_1)

for i in range(2):
    for j in range(4):
        sum_array += array[i][j]
        avg_array = sum_array / 4
    print(float(int(avg_array)), end=' ')
    sum_array = 0

print()

for i in range(4):
    for j in range(2):
        sum_array += array[j][i]
    avg_array = sum_array / 2
    print(float(int(avg_array)), end=' ')
    sum_array = 0

print()

sum_total = 0

for i in range(2):
    for j in range(4):
        sum_total += array[i][j]

avg_total = sum_total / 8

print(float(int(avg_total)))