s = list(input())

t = 0

for i in s:
    if 57 >= ord(i) >= 48:
        t += int(i)
        
print(t)