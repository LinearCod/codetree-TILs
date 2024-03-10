def find_max_unique(nums):
    num_count = {}
    
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    max_unique = -1
    
    for num, count in num_count.items():
        if count == 1 and num > max_unique:
            max_unique = num
    
    return max_unique

# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 중복되지 않는 숫자 중 최댓값 찾기
result = find_max_unique(numbers)

# 결과 출력
print(result)