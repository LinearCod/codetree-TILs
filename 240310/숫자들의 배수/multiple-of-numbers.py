n = int(input())

cnt_1 = 1
cnt_2 = 0

arr = []

while True:
    if n * cnt_1 % 5 == 0:
        cnt_2 += 1
    arr.append(n * cnt_1)
    cnt_1 += 1
    if cnt_2 == 2:
        break

for i in arr:
    print(i, end=' ')