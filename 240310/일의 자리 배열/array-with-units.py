arr = list(map(int, input().split()))

for _ in range(8):
    if arr[-1] + arr[-2] >= 10:
        num = str(arr[-1] + arr[-2])
        num = int(num[-1])
        arr.append(num)
    else:
        arr.append(arr[-1] + arr[-2])

for i in arr:
    print(i, end=' ')