t = input().split()
s, q = t[0], int(t[1])

result = s

cnt = 0

for _ in range(q):
    tmp = input().split()
    if int(tmp[0]) == 1:
        a, b = int(tmp[1]), int(tmp[2])
        if s == result:
            arr = list(s)
            word_1, word_2 = arr[a - 1], arr[b - 1]
            arr[a - 1], arr[b - 1] = word_2, word_1
            result = ''.join(arr)
            print(result)
        else:
            arr = list(result)
            word_1, word_2 = arr[a - 1], arr[b - 1]
            arr[a - 1], arr[b - 1] = word_2, word_1
            result = ''.join(arr)
            print(result)
    else:
        a, b = tmp[1], tmp[2]
        cnt = 0
        if s != result:
            for i in arr:
                if i == a:
                    arr[cnt] = b
                cnt += 1
            result = ''.join(arr)
            print(result)
        else:
            arr = list(s)
            for i in arr:
                if i == a:
                    arr[cnt] = b
                cnt += 1
            result = ''.join(arr)
            print(result)