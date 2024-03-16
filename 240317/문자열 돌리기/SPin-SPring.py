word_1 = input()

cnt = 0

print(word_1)

while True:
    if cnt == 0:
        word = word_1[-1] + word_1[:-1]
    else:
        word = word[-1] + word[:-1]
    if word == word_1:
        print(word)
        break
    cnt += 1
    print(word)