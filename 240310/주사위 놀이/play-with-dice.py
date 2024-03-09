arr = list(map(int, input().split()))

arr_1 = [0] * 6

for i in arr:
    arr_1[i - 1] += 1

for i in range(1, 7):
    print(f'{i} - {arr_1[i-1]}')