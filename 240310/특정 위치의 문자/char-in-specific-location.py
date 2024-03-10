word = input()

arr = ['L', 'E', 'B', 'R', 'O', 'S']

cnt = 'None'

for i, char in enumerate(arr):
    if char == word:
        cnt = i

print(cnt)