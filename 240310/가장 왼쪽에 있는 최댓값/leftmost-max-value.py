n = int(input())

arr = list(map(int, input().split()))

max_val = max(arr)

break_1 = 'N'

while arr != []:
    for i in arr:
        if arr == []:
            break
        max_val = max(arr)
        if i == max_val:
            print(arr.index(i) + 1, end=' ')
            arr = arr[:arr.index(i)]
            max_val = 0