word_a = input()
word_b = input()

idx = word_a.index(word_b)

arr = list(word_a)

while True:
    if idx == -1:
        print(''.join(arr))
        break
    elif arr == []:
        break
    else:
        a = arr[0:idx]
        b = arr[idx + len(word_b):]
        arr = a + b
        s = ''.join(arr)
        idx = s.find(word_b)