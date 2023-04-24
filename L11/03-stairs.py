def stair(n):
    if n  == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stair(n-1)+stair(n-2)+stair(n-3)
n = int(input('n : '))
print(stair(n))