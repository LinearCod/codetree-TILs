num_inp = input()
num = num_inp.split()
a, b = int(num[0]), int(num[1])
print(a + b, '\n', a - b, '\n', a//b, '\n', a%b, sep = '')