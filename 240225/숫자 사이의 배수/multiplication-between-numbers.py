a,b = map(int, input().split())
c,d= 0,0
for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        c += i
        d += 1
print(c, f'{c/d:.1f}')