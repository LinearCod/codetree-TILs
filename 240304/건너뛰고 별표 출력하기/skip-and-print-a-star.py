n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    for _ in range(2):
        print()
        
for i in range(n-1, -1, -1):
    for j in range(i):
        print('*', end='')
    for _ in range(2):
        print()