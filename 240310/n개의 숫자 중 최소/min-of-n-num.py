n = int(input())

arr = list(map(int, input().split()))

cnt = 0

a = arr[0]

for i in arr[1:]:
    if a > i:
        a = i

for i in arr[1:]:
    if a == i:
        cnt += 1

print(a, cnt)