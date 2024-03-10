n1,n2 = list(map(int, input().split()))

arr_A = list(map(int, input().split()))

arr_B = list(map(int, input().split()))

leng_A = len(arr_A)

leng_B = len(arr_B)

cnt = arr_A.count(arr_B[0])

start_a = []

if cnt == 1:
    idx = arr_A.index(arr_B[0])
    New_A = arr_A[idx:idx + leng_B + 1]
    if New_A == arr_B:
        print('Yes')
    else:
        print('No')
else:
    for i in range(leng_A):
        if arr_A[i] == arr_B[0]:
            start_a.append(i)
    for i in start_a:
        if leng_B > len(arr_A[i:]):
            break
        else:
            New_a = arr_A[i:i + leng_B]
            if New_a == arr_B:
                print('Yes')
            else:
                print('No')