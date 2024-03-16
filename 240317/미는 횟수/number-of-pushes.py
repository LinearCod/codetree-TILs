a = input()

b = input()

cnt = 0

if a == b:
    print(cnt)
else:
    while True:
        if cnt == 0 and len(a) != 3:
            a_1 = a[1:] + a[0]
            cnt += 1
        elif len(a) == 3:
            a_2 = a[-1] + a[0:2]
            cnt += 1
            if a_2 == b:
                print(cnt)
                break
        elif cnt != 0 and len(a) != 3:
            a_1 = a_1[1:] + a_1[0]
            cnt += 1
            if a_1 == a:
                print(-1)
                break
            if a_1 == b:
                print(cnt)
                break