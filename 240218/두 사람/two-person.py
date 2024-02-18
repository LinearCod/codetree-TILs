num1_inp = input()
num2_inp = input()
num1 = num1_inp.split()
num2 = num2_inp.split()
a1,s1 = int(num1[0]), num1[1]
a2,s2 = int(num2[0]), num2[1]
if a1 >= 19 or a2 >= 19:
    if a1 >= 19 and s1 == 'M':
        print('1')
    elif a2 >= 19 and s2 == 'M':
        print('1')
    else:
        print('0')
else:
    print('0')