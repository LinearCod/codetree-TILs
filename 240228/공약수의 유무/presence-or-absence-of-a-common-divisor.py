a,b = map(int, input().split())

booly = False

for i in range(a,b+1):
    if 1920 % i and 2880 % i:
        booly = True

if booly == True:
    print('1')
else:
    print('0')