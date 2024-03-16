t = input().split()

n, s = int(t[0]), t[1]

cnt = 0

for _ in range(n):
    k = input()
    if k == s:
        cnt += 1
        
print(cnt)