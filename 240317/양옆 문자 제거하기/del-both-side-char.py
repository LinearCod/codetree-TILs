word = input()

arr = list(word)

arr.pop(1)

arr.pop(-2)

s = ''.join(arr)

print(s)