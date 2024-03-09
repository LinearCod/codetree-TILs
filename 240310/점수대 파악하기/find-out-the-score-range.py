arr = list(map(int, input().split()))

arr_1 = [0] * 10

for i in arr:
    if 100 > i >= 10:
        t = int(str(i)[0])
        arr_1[-t] += 1
    elif i == 100:
        arr_1[0] += 1
    elif i == 0:
        break

for i in range(10, 0, -1):
    print(f'{i * 10} - {arr_1[10 - i]}')