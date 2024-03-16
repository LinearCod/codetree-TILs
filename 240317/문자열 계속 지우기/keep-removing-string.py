word_a = input()
word_b = input()

idx = word_a.index(word_b)

arr = list(word_a)

while True:
    if idx == -1:
        print(''.join(arr))
        break
    else:
        arr = arr[0:idx] + arr[idx + len(arr):]
        s = ''.join(arr)
        idx = s.find(word_b)