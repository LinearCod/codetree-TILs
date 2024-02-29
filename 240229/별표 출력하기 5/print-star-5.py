N = int(input())
lst = []
for i in range(N,0,-1):
    lst = ['*' * i]
    lst += lst * (i-1)  
    print(*lst)