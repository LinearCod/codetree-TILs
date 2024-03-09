arr = list(map(int, input().split()))

sum_odd, sum_even = 0, 0

for i in range(0, 9, 2):
    sum_odd += arr[i]
    
for i in range(1, 10, 2):
    sum_even += arr[i]
    
if sum_odd > sum_even:
    print(sum_odd - sum_even)
elif sum_odd < sum_even:
    print(sum_even - sum_odd)