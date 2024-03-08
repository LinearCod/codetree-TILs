arr = list(map(int, input().split()))

arr_1, arr_2= [], []

for i in arr[1::2]:
    arr_1.append(i)

for i in arr[2:9:3]:
    arr_2.append(i)
    
print(f'{sum(arr_1)} {sum(arr_2) / len(arr_2):.1f}')