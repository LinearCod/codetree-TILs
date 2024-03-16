word_a = input()
word_b = input()

cnt = 0

for i in range(len(word_a) - 1):
    if word_a[i:i + 2] == word_b:
        cnt += 1

print(cnt)