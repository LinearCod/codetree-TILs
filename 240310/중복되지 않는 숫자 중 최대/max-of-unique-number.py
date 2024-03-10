n = int(input())

arr = list(map(int, input().split()))

max_val = 0

t = 7

for i in arr:
    if i > max_val:
        max_val = i

arr_count = arr.count(max_val)

while True:
    if arr_count != 1 and t != 0:
        for _ in range(arr_count):
            if max_val not in arr:
                t = 0
                break
            arr.remove(max_val)
            if arr == []:
                t = 0
                break
    elif t == 0:
        print(-1)
        break
    elif arr_count == 1 and t != 0:
        print(max(arr))
    arr_count = arr.count(max(arr))