n = int(input())
a = 1
for i in range(1,5001):
    if i == 1:
        a = n // i
    a = a // i
    if a <= 1:
        break
print(i)