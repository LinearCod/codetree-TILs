while True:
    inp = input().split()
    a,b = int(inp[0]), int(inp[1])
    print(a*b)
    if inp[2] == 'C':
        break