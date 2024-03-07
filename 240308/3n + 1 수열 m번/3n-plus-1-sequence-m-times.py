m = int(input())

for _ in range(m):
    cnt = 0
    n = int(input())
    while n != 1:
        if n % 2 == 0:
            n //= 2
            cnt += 1
        else:
            n = 3 * n + 1 
            cnt += 1
    print(cnt)