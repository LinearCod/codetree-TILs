n = int(input())
a = 0
while True:
    if n % 2 == 0:
        n = n/2
    elif n % 2 != 0:
        if n == 1:
            print(a)
            break
        else:
            n = 3*n+1
    a += 1