word_input = input()
word_target = input()

if word_target in word_input:
    print(word_input.index(word_target))
else:
    print(-1)