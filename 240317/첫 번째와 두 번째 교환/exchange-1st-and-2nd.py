word = input()

arr = list(word)

cnt = 0

a, b = arr[0], arr[1]

for i in arr:
    if i == a:
        arr[cnt] = b
    elif i == b:
        arr[cnt] = a
    cnt += 1
    
s = ''.join(arr)

print(s)