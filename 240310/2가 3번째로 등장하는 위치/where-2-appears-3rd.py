n = int(input())

arr = list(map(int, input().split()))

idx = 1

cnt = 0

for i in arr:
    if i == 2:
        cnt += 1
        if cnt == 3:
            break
    idx += 1

print(idx)