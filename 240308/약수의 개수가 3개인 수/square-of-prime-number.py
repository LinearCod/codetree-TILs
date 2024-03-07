start,end = map(int, input().split())

cnt_1 = 0
cnt_2 = 0

for i in range(start, end+1):
    cnt_1 = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt_1 += 1
    if cnt_1 == 3:
        cnt_2 += 1
print(cnt_2)