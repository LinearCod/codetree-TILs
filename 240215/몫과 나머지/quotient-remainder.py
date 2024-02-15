temp_num = input()
num = temp_num.split()
a, b = int(num[0]), int(num[1])
print(a//b, a%b, sep = '...')