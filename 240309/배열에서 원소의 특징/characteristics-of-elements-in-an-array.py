arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i % 3 == 0:
        print(arr[cnt - 1])
        break
    cnt += 1