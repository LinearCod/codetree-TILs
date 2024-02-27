a = 0
while True:
    n = int(input())
    if n % 2 != 0:
        pass
    elif n % 2 == 0:
        print(n // 2)
        a += 1
        if a == 3:
            break