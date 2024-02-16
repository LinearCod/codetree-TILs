inp = input()
num = inp.split()
height, weight = map(int, num)
h = height/100
bmi = int(weight/(h**2))
print(bmi)
if bmi >= 25:
    print('Obesity')