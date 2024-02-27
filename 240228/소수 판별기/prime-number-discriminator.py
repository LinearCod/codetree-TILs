n = int(input())

booly = False

for i in range(2,n):
    if n % i == 0:
        booly = True

if booly == False:
    print('P')
else:
    print('C')