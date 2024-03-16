alpha = input()

arr_word = ['apple', 
            'banana', 
            'grape',
            'blueberry',
            'orange'
            ]

cnt = 0

for i in arr_word:
    if i[2] == alpha or i[3] == alpha:
        print(i)
        cnt += 1

print(cnt)