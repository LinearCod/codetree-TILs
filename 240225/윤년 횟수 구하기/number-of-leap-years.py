n = int(input())
a = 0
for i in range(1,n+1):
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                a += 1
            else:
                pass
        else:
            a += 1
    else:
        pass
print(a)