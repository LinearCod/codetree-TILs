a,b,c = map(int, input().split())

booly = 0

for i in range(a,b+1):
    if i % c == 0:
        booly = 1
        
if booly == 1:
    print('YES')
else:
    print('NO')