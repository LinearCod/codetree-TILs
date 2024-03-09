a,b = map(int, input().split())

arr = [0] * b

a_list = [a]
b_list = []

while True:
    if a_list[-1] == a:
        a_list.append(a // b)
        b_list.append(a % b)
    else:
        a_list.append(a_list[-1] // b)
        b_list.append(a_list[-1] % b)
        if a_list[-1] == 0:
            break

for i in b_list:
    arr[i] += 1

result = [i ** 2 for i in arr]

print(sum(result))