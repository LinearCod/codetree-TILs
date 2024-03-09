arr = list(map(int, input().split()))

arr_1 = []

for i in arr:
    if i % 2 != 0 and i != 0:
        arr_1.append(i + 3)
    elif i % 2 == 0 and i != 0:
        arr_1.append(i // 2)
    else:
        pass

for i in arr_1:
    print(i, end=' ')