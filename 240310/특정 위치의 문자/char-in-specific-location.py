word = input()

arr = ['L', 'E', 'B', 'R', 'O', 'S']

cnt = 0

for i in arr:
    if i == word:
        break
    cnt += 1

if word not in arr:
    print('None')
else:
    print(cnt)