n = int(input())

arr = list(map(int, input().split()))

arr_1 = [ i ** 2 for i in arr]

for i in arr_1:
    print(i, end=' ')