n = int(input())

lit = []

sum_1 = 0
cnt = 0

for _ in range(n):
    lit.append(input())
    
alpha = input()

for i in lit:
    if i[0] == alpha:
        sum_1 += len(i)
        cnt += 1
        
print(f'{cnt} {sum_1 / cnt:.2f}')