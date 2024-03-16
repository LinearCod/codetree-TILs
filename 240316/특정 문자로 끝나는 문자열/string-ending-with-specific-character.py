lit = []

for _ in range(10):
    lit.append(input())

alpha = input()

cnt = 0

for i in lit:
    if i[-1] == alpha:
        print(i)
        cnt += 1
    
if cnt == 0:
    print('None')