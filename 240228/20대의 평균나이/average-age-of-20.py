a = 0
b = 0
while True:
    n = int(input())
    if  n > 29 or n < 20:
        print(f'{a/b:.2f}')
        break
    a += n
    b += 1