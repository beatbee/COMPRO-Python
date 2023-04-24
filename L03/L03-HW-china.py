def plus(total,value):
    total += value
    return total

def minus(total,value):
    total -= value
    return total

n = int(input("How many food you have : "))
total = 0
x = 0
for i in range(n):
    a,b = [int(x) for x in input().split()]
    if b == 1:
        x = x + plus(total,a)
    elif b == -1:
        x = x + minus(total,a)
print(x)