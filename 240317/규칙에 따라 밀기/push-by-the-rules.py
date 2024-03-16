word = input()

order = list(input())

for i in order:
    if i == 'L':
        word = word[1:] + word[0]
    else:
        word = word[-1] + word[:-1]

print(word)