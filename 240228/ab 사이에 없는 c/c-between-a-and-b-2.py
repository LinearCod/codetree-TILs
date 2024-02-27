a,b,c = map(int, input().split())

booly = True

for i in range(a,b+1):
    if i % c != 0:
        if c % i == 0:
            continue
        booly = False

if booly == True:
    print('NO')
else:
    print('YES')