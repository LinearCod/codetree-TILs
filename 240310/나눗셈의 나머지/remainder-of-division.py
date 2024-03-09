a, b = map(int, input().split())

remain = []
remain_num = [0] * b
cnt = 0

while True:
    remain.append(a % b)
    if a // b == 0:
        break
    a //= b

for i in remain:
    remain_num[i] += 1

for i in remain_num:
    cnt += i ** 2

print(cnt)