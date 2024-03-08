n = int(input())

cnt = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    mean_val = int(sum(arr) / 4)
    if mean_val >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(cnt)