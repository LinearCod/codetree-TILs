a,b,c = map(int, input().split())

booly = False

for i in range(a,b+1):
    if i % c != 0.000:
        booly = True

if booly == True:
    print('YES')
else:
    print('NO')