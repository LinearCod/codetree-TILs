a = int(input())
for i in range(1,a+1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    b = i // 8
    if b % 2 == 0:
        continue
    if i % 7 < 4:
        continue
    print(i, end=' ')