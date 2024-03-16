word = input()

arr = list(word)

t = len(arr)

while True:
    n = int(input())
    if len(arr) == 1:
        break
    if n > t:
        arr.pop(-1)
        print(''.join(arr))
    arr.pop(n)
    print(''.join(arr))