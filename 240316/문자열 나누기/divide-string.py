n = int(input())

word = ''

cnt = 0

num = input().split()

for i in num:
    word += i

for i in word:
    if cnt % 5 == 0 and cnt != 0:
        print()
    print(i, end='')
    cnt += 1