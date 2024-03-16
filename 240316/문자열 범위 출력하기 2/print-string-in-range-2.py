word = input()
num = int(input())

if num > len(word):
    print(word[-1::-1])
else:
    print(word[-1:- num - 1:-1])