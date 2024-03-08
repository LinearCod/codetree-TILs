arr = list(map(int, input().split()))

arr_1 = []

for i in arr:
    if i == 0:
        break
    arr_1.append(i)
    
print(f'{sum(arr_1)} {sum(arr_1) / len(arr_1):.1f}')