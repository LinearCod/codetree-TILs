num_inp = input()
num = num_inp.split()
a,b,c = int(num[0]), int(num[1]), int(num[2])
sum_t = a+b+c
avg_t = int((a+b+c)/3)
sub_t = sum_t - avg_t
print(f'{sum_t}\n{avg_t}\n{sub_t}')