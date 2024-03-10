n = int(input())

arr = list(map(int, input().split()))

max_val_1 = 0

max_val_2 = 0

for i in arr:
    if i > max_val_1:
        max_val_1 = i

arr.remove(max_val_1)

for i in arr:
    if i > max_val_2:
        max_val_2 = i

print(max_val_1, max_val_2)