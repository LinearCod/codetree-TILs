word = input()

arr = list(word)

arr[1], arr[-2] = 'a', 'a'

s = ''.join(arr)

print(s)