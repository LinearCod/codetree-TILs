cnt = [0] * 4

for _ in range(3):
    arr = input().split()
    c = arr[0] 
    t = int(arr[-1])
    if c == 'Y' and t >= 37:
        cnt[0] += 1
        if cnt [0] >= 2:
            cnt.append('E')
    elif c == 'N' and t >= 37:
        cnt[1] += 1
    elif c == 'Y' and t < 37:
        cnt[2] += 1
    else:
        cnt[3] += 1

for i in cnt:
    print(i, end=' ')