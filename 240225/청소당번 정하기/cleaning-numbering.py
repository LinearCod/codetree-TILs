n = int(input())
a,b,c = 0,0,0
for i in range(1,n+1):
    if i % 2 == 0 and i % 3 != 0 and i % 12 != 0:
        a += 1
    if i % 3 == 0 and i % 12 != 0:
        b += 1
    if i % 12 == 0:
        c += 1
print(a,b,c)