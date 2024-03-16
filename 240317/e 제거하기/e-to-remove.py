word = input()

idx = word.index('e')

lit = list(word)

lit.pop(idx)

s = ''.join(lit)

print(s)