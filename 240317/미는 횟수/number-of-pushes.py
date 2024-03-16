a = input()

b = input()

cnt = 0

if a == b:
    print(cnt)
else:
    while True:
        if cnt == 0:
            a_1 = a[1:] + a[0]
            cnt += 1
        else:
            a_1 = a_1[1:] + a_1[0]
            if a_1 == a:
                print(-1)
                break
            if a_1 == b:
                print(cnt + 1)
                break
            cnt += 1