def stair(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stair(n-a)+stair(n-b)+stair(n-c)
n = int(input('n : '))
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
print(stair(n))