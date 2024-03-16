word_1 = input()
word_2 = input()
word_3 = input()

arr = [len(word_1), len(word_2), len(word_3)]

print(max(arr) - min(arr))