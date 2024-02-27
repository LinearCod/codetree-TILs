a,b,c = map(int, input().split())

booly = False

for i in range(a,b+1):
    if i % c != 0:
        if type(i % c) == float:
            pass
        else:
            booly = True

if booly == True:
    print('YES')
else:
    print('NO')