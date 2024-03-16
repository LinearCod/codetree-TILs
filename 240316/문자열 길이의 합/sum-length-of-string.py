n = int(input())

cnt_1, cnt_2 = 0, 0

for _ in range(n):
    word = input()
    cnt_1 += len(word)
    if word[0] == 'a':
        cnt_2 += 1
    
print(cnt_1, cnt_2)