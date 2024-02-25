a,b = 0, 0
for _ in range(10):
    n = int(input())
    if 200 >= n >= 0:
        a += n
        b += 1
print(a,f'{a/b:.1f}')