str_1 = input()
str_2 = input()

arr = []

def strip_str(word):
    for i in word:
        if i == ' ':
            continue
        else:
            arr.append(i)

strip_str(str_1)

strip_str(str_2)

for i in arr:
    print(i, end='')