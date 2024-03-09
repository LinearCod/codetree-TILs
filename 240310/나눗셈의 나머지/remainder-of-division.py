a, b = map(int, input().split())

remain = []
remain_num = [0] * b
cnt = 0

while True:
    if a <= 1:
        break
    remain.append(a % b)
    a //= b

for i in remain:
    remain_num[i] += 1

for i in remain_num:
    cnt += i ** 2

print(cnt)