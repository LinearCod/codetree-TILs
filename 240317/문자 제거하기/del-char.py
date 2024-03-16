word = input()

arr = list(word)

while True:
    n = int(input())
    if arr == []:
        break
    if n > len(arr):
        arr.pop(-1)
        print(''.join(arr))
    arr.pop(n)
    print(''.join(arr))