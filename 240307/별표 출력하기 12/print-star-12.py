n = int(input())

cnt_1 = 1

cnt_2 = 2

for i in range(n):
    for j in range(n):
        if i == 0:
            print('* ', end='')
        elif i % 2 != 0:
            if j >= cnt_1 and j % 2 != 0:
                print('* ', end='') 
            else:
                print('  ', end='')
        elif i != 0 and i % 2 == 0:
            if j >= cnt_2 and j % 2 != 0:
                print('* ', end='')
            else:
                print('  ', end='')
    if i != 0 and i % 2 != 0 :
        cnt_1 += 2
    elif i != 0 and i % 2 == 0:
        cnt_2 += 2
    print()