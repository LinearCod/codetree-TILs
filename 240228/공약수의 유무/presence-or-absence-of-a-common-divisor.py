a,b = map(int, input().split())

booly = False

for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        booly = True

if booly == True:
    print('1')
else:
    print('0')