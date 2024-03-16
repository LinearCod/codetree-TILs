cnt = 0

lit = []

while True:
    s = input()
    if s == '0':
        break
    elif cnt % 2 == 0:
        lit.append(s)
    cnt += 1
        
print(cnt)

for i in lit:
    print(i)