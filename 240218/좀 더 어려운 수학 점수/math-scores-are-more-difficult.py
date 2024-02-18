m_a,e_a = map(int, input().split())
m_b,e_b = map(int, input().split())
if m_a > m_b:
    print('A')
elif m_a == m_b:
    if e_a > e_b:
        print('A')
    else:
        print('B')
else:
    print('B')