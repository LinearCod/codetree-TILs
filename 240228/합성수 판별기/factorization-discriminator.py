n = int(input())

booly = False

if n == 1:
    print('N')
    
for i in range(2,n+1):
    if n % i == 0:
        booly = True

if booly == True:
    print('C')
else:
    print('N')