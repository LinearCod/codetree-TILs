n = int(input())

arr = list(map(int, input().split()))

dis = []

for i in arr:
    for j in arr:
        if i - j > 0:
            dis.append(i - j)

print(min(dis))