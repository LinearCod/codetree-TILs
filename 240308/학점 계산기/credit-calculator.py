n = int(input())

arr = list(map(float, input().split()))
    
mean_val = sum(arr) / len(arr)

if int(mean_val) >= 4:
    print(f'{mean_val:.1f}')
    print('Perfect')
elif 4 > int(mean_val) >= 3:
    print(f'{mean_val:.1f}')
    print('Good')
else:
    print(f'{mean_val:.1f}')
    print('Poor')