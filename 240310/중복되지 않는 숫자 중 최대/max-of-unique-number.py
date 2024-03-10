n = int(input())

arr = list(map(int, input().split()))

arr.sort()

max_val = arr[-1]

cnt = 0

for i in arr[-1::-1]:
    if max_val == i:
        cnt += 1

if cnt != 1:
    print(-1)
else:
    print(max_val)