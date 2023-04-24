def hammer(a):
    print(' '+'o'*(3*a+4))
    for i in range(2*a+1):
        print('o'*(3*a+6))
    print(' '+'o'*(3*a+4))
    for i in range(a+2):
        print(' '*(a+3)+'o'*(a))
    for i in range(a):
        print(' '*(a+2) +'o'*(a+2))
    print(' '*(a+3)+'o'*(a))

n = float(input("Input Gold: "))
if n<1000:
    print("Not enough gold.")
elif n<2000:
    hammer(1)
elif n<3000:
    hammer(2)
elif n<4000:
    hammer(3)
else:
    hammer(4)


    