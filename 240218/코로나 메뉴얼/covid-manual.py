a = input().split()
b = input().split()
c = input().split()
C_a,T_a = a[0], int(a[1])
C_b,T_b = b[0], int(b[1])
C_c,T_c = c[0], int(c[1])
if C_a == 'Y' and T_a >= 37:
    if C_b == 'Y' and T_b >= 37:
        print('E')
    elif C_c == 'Y' and T_c >= 37:
        print('E')
    else:
        print('N')
elif C_b == 'Y' and T_b >= 37:
    if C_c == 'Y' and T_c >= 37:
        print('E')
    else:
        print('N')
else:
    print('N')