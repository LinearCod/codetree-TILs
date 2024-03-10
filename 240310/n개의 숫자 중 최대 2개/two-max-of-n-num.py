n = int(input())

arr = list(map(int, input().split()))

arr.sort()

max_val_1, max_val_2 = arr[-1], arr[-2]

print(max_val_1, max_val_2)