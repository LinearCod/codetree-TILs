word = input()

word = word[1:len(word):2]

for i in word[-1::-1]:
    print(i, end='')