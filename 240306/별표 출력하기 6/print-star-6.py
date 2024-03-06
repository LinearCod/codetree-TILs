n = int(input())

cnt = 0

for i in range(n):
    lit = []
    
    lit.append('* '*(-2*i+(2*n-1)))
    
    for j in range(cnt):
        print('  ', end='')
    
    for j in lit:
        print(j, end='')
        
    print()
    
    cnt += 1

cnt = n - 2

for i in range(n-1):
    lit = []
    
    lit.append('* '*(2*i+3))
    
    for j in range(cnt):
        print('  ', end='')
        
    for j in lit:
        print(j, end='')
        
    print()
    
    cnt -= 1