arr = list(map(int, input().split()))

arr_1 = []

for i in arr:
    if i == 0:
        print(sum(arr_1[-1:-4:-1]))
        break
    arr_1.append(i)