s = list(input())

for i in s:
    if 'Z' >= i >= 'A':
        print(i.lower(), end='')
    elif 'z' >= i >= 'a':
        print(i.upper(), end='')