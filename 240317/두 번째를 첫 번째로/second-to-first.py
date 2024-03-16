word = input()

arr = list(word)

cnt = 0

alpha_1, alpha_2 = arr[0], arr[1]

for i in word:
    if i == alpha_2:
        arr[cnt] = alpha_1
    cnt += 1

s = ''.join(arr)

print(s)