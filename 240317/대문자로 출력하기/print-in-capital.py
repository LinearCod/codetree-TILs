s = list(input())

for i in s:
    if 'Z' >= i >= 'A' or 'z' >= i >= 'a':
        print(i.capitalize(), end='')