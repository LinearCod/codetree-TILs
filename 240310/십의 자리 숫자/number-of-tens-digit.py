arr = list(map(int, input().split()))

arr_1 = []

arr_2 = [0] * 9

for i in arr:
    if i == 0:
        break
    else:
        arr_1.append(i)

for i in arr_1:
    if i >= 10:
        t = int(str(i)[0])
        arr_2[t - 1] += 1
    else:
        pass

for i in range(1, 10):
    print(f'{i} - {arr_2[i - 1]}')