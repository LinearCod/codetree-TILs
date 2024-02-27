'''
n = int(input())
cnt = 0
while n <= 1000:
    if n % 2 == 0:
        n = 3 * n + 1
    elif n % 2 != 0:
        n = 2 * n + 2
    cnt += 1
print(cnt)
'''

a,b,c = map(int, input().split())

for i in range(a,b+1):
    if i % c == 0:
        boolean = True
        
if boolean == True:
    print('YES')
else:
    print('NO')