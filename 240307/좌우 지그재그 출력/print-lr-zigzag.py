n = int(input())

cnt_1 = 1
cnt_2 = n * 2

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cnt_1, end=' ')
            cnt_1 += 1
            if j == n - 1:
                cnt_1 += n
        else:
            print(cnt_2, end=' ')
            cnt_2 -= 1
            if j == n - 1:
                cnt_2 = 2*n*(i + 1)
    print()