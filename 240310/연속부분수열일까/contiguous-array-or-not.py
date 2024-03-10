n1,n2 = list(map(int, input().split()))

arr_A = list(map(int, input().split()))

arr_B = list(map(int, input().split()))

leng_A = len(arr_A)

leng_B = len(arr_B)

cnt_1 = arr_A.count(arr_B[0])

cnt_2 = 0

cnt_3 = 0

start_a = []

if cnt_1 == 1 and leng_B != 1:
    idx = arr_A.index(arr_B[0])
    New_A = arr_A[idx:idx + leng_B]
    if New_A == arr_B:
        print('Yes')
    else:
        print('No')
elif cnt_1 != 1 and leng_B != 1:
    for i in range(leng_A):
        if arr_A[i] == arr_B[0]:
            start_a.append(i)
    for i in start_a:
        if leng_B > len(arr_A[i:]):
            break
        else:
            New_a = arr_A[i:i + leng_B]
            if New_a == arr_B:
                cnt_2 += 1
            else:
                pass
    if cnt_2 != 0:
        print('Yes')
    else:
        print('No')
elif leng_B == 1:
    for i in arr_A:
        if i == arr_B[0]:
            cnt_3 += 1
    if cnt_3 == 0:
        print('No')
    else:
        print('Yes')

# 4 1
# 1 2 5 2
# 3