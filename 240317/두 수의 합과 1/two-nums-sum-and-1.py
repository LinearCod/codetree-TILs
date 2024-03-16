a, b = tuple(input().split())

c = int(a) + int(b)

cnt = 0

for i in str(c):
    if i == '1':
        cnt += 1
    
print(cnt)