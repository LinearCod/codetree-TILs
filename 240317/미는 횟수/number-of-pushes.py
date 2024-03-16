def min_shift_to_match(A, B):
    n = len(A)
    for shift in range(1, n + 1):
        shifted_A = A[-shift:] + A[:-shift]  # 우측으로 shift 만큼 이동
        if shifted_A == B:
            return shift
    return -1  # 문자열 A를 우측으로 밀어서 B와 같아지는 경우가 없는 경우

# 입력
A = input().strip()
B = input().strip()

# 출력
print(min_shift_to_match(A, B))