s = list(input())

for i in s:
    if 'z' >= i >= 'a':
        print(i, end='')
    elif 'Z' >= i >= 'A':
        print(i.lower(), end='')
    elif 57 >= ord(i) >= 48:
        print(i, end='')