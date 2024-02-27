n = int(input())
a = 0
while True:
    n = n / 2
    a += 1
    if n == 1:
        print(a)
        break