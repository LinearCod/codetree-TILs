booly_1 = False
booly_2 = True
num_list = []

for _ in range(5):
    n = int(input())
    num_list.append(n)

for i in range(5):
    if num_list[i] % 3 == 0:
        booly_1 = True
    else:
         booly_2 = False

if booly_1 == True and booly_2 == True:
    print('1')
else:
    print('0')