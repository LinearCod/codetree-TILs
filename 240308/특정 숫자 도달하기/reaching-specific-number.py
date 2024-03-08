lit = list(map(int, input().split()))

lit_1 = []

for i in lit:
    if i >= 250:
        break
    lit_1.append(i)

print(f'{sum(lit_1)} {sum(lit_1) / len(lit_1):.1f}')