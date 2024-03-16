word, alpha = map(str, input().split())

if alpha in word:
    print(word.index(alpha))
else:
    print('No')