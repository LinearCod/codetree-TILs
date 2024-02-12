a=float(input())
b=float(input())
c=float(input())
print(round(a,3))
print(round(b,3))
t=str(round(c,3))
if t[-1]=='0':
    print(t+'00')
else:
    print(round(c,3))