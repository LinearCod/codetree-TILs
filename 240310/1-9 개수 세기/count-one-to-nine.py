n = int(input())

arr = list(map(int, input().split()))

cnt = 1

cnt_arr = [0] * 9

for _ in range(9):
    for i in arr:
        if i == cnt:
            cnt_arr[i-1] += 1
    cnt += 1

for i in cnt_arr:
    print(i)