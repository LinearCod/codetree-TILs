n = int(input())

arr = [1]

arr.append(n)

while True:
    arr.append(arr[-1] + arr[-2])
    if arr[-1] + arr[-2] >= 100:
        arr.append(arr[-1] + arr[-2])
        for i in arr:
            print(i, end=' ')
        break