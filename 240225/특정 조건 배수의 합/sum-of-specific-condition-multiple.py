a,b = map(int, input().split())
c,d = 0,0
if a < b:
    for i in range(a,b+1):
        if i % 5 == 0:
            c += i
elif a > b:
    for i in range(b,a+1):
        if i % 5 == 0:
            d += i
print(c+d)