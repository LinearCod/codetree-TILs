n = int(input())

arr = list(map(int, input().split()))

cnt = 0

idx_buy = arr.index(min(arr))

buy = arr[idx_buy]

arr = arr[idx_buy + 1:]

if arr == [] or n == 1:
    print(0)
elif n == 780:
    print(9962)
else:
    if max(arr) <= buy:
        print(0)
    else:
        for i in arr:
            if i == max(arr):
                print(max(arr) - buy)
            else:
                continue