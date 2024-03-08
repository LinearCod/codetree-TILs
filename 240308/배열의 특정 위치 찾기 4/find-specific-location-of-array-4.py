arr = list(map(int, input().split()))

arr_1 = []
arr_2 = []
cnt = 0

for i in arr:
    if i == 0:
        break
    arr_1.append(i)
    
for i in arr_1:
    if i % 2 == 0:
        cnt += 1
        arr_2.append(i)

print(f'{cnt} {sum(arr_2)}')