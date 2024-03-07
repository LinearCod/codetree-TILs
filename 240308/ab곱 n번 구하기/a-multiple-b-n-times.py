n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    
    t = 1
    
    for i in range(a, b+1):
        t *= i
        
    print(t)