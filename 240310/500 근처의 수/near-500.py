arr = list(map(int, input().split()))

arr_1 = []

arr_2 = []

for i in arr:
    if i > 500:
        arr_1.append(i)
    elif i < 500:
        arr_2.append(i)

print(max(arr_2), min(arr_1))