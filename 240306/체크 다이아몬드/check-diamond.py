n = int(input())

cnt = n - 1

for i in range(n):
    lit = []
    
    lit.append('* '*(i+1))
    
    for j in range(cnt):
        print(' ', end='')
        
    for j in lit:
        print(j, end='')
        
    print()
    
    cnt -= 1

cnt = 1

for i in range(n-1):
    lit = []
    
    lit.append('* '*(-1*i+(n-1)))
    
    for j in range(cnt):
        print(' ', end='')
        
    for j in lit:
        print(j, end='')
    
    cnt += 1
    
    print()