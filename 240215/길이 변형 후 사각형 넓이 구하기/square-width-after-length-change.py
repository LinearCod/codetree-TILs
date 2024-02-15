num_inp = input()
num = num_inp.split()
width = int(num[0]) + 8
length = int(num[1]) * 3
area = width * length
print(width, '\n', length, '\n', area, sep = '')