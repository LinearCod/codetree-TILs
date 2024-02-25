n = int(input())
a,b = 0,0
for i in range(n):
    m = int(input())
    a += m
    b += 1
print(a,f'{a/b:.1f}')