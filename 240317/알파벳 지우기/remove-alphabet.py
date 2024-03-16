s1 = list(input())
s2 = list(input())

a = ''
b = ''

for i in s1:
    if 57 >= ord(i) >= 48:
        a += i

for i in s2:
    if 57 >= ord(i) >= 48:
        b += i

print(int(a) + int(b))