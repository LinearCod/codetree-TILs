word = input().split()

word_1 = word[1]

arr = list(word_1)

arr[0], arr[1] = word[0][0], word[0][1]

s = ''.join(arr)

print(s)