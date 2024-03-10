n,q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    question = list(map(int, input().split()))
    type_q = question[0]
    if type_q == 1:
        print(arr[question[1] - 1])
    elif type_q == 2:
        cnt = arr.count(question[1])
        if cnt == 0:
            print(0)
        else:
            idx = arr.index(question[1])
            print(idx + 1)
    else:
        for i in range(question[1], question[-1] + 1):
            print(arr[i - 1], end=' ')