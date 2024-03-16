a, b = tuple(input().split())

lit = []

for i in a:
    if 57 < ord(i) or ord(i) < 48:
        break
    else:
        lit.append(i)

num_1 = int(''.join(lit))

lit = []

for i in b:
    if 57 < ord(i) or ord(i) < 48:
        break
    else:
        lit.append(i)

num_2 = int(''.join(lit))

print(num_1 + num_2)