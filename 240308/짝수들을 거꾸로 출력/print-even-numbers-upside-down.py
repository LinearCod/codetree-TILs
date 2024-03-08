n = int(input())

arr = list(map(int, input().split()))

arr_1 = []

for i in arr:
    if i % 2 == 0:
        arr_1.append(i)

for i in arr_1[::-1]:
    print(i, end=' ')