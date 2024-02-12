a=float(input())
b=float(input())
c=float(input())
i=str(round(a,3))
j=str(round(b,3))
k=str(round(c,3))
if i[-1]=='0':
    print(i+'00')
else:
    print(round(a,3))
if j[-1]=='0':
    print(j+'00')
else:
    print(round(b,3))
if k[-1]=='0':
    print(k+'00')
else:
    print(round(c,3))