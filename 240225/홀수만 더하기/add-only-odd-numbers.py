n = int(input())
a = 0
for i in range(n):
    b = int(input())
    if b % 3 == 0 and b % 2 != 0:
        a += b
print(a)