word = input()

cnt = 1
cnt_1 = 0

lit = []

for i in word:
    if cnt >= len(word):
        lit.append(f'{i}')
        if cnt_1 + 1 >= 10:
            for j in str(cnt_1 + 1):
                lit.append(j)
        else:
            lit.append(f'{cnt_1 + 1}')
        break
    if i == word[cnt]:
        cnt_1 += 1
    else:
        lit.append(f'{i}')
        if cnt_1 + 1 >= 10:
            for j in str(cnt_1 + 1):
                lit.append(j)
        else:
            lit.append(f'{cnt_1 + 1}')
        cnt_1 = 0
    cnt += 1
    
print(len(lit))

for i in lit:
    print(i, end='')