n = int(input())
a = []
for i in range(n):
    a = []
    a.append('*'*(n-i))
    a[0] += ' '
    print(a[0]*(n-i), end='')
    print()