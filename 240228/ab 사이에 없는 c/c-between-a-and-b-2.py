a,b,c = map(int, input().split())

booly = 1

for i in range(a,b+1):
    if i % c != 0:
        if type(i % c) == float:
            booly = 1
        else:
            booly = 0

if booly == 1:
    print('YES')
else:
    print('NO')