array = []

sum_value = 0

cnt = 1

for _ in range(4):
    array.append(list(map(int, input().split())))

for i in range(4):
    for j in range(cnt):
        sum_value += array[i][j]
    cnt += 1
        
print(sum_value)