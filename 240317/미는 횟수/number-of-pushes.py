a = input()

b = input()

cnt = 0

if a == b:
    print(cnt)
else:
    while True:
        if cnt == 0:
            a_1 = a[1:] + a[0]
            b_1 = b[1:] + b[0]
            cnt += 1
        else:
            if a_1 == b:
                print(cnt)
                break
            if b_1 == a:
                print(cnt)
                break
            if a_1 == a:
                print(-1)
                break
            a_1 = a_1[1:] + a_1[0]
            b_1 = b_1[1:] + b_1[0]
            cnt += 1