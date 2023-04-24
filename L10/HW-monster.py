import numpy as np
X = np.random.RandomState(1)
b = int(input('Blood Start: '))
monh = b
meh = b
ch = 0
while True:
    myTurn = input('Attack(a) or Heal(h): ')
    if myTurn == 'a':
        if ch == 0:
            at = 10
            ch = 1
        elif ch == 1:
            at+=2
        monh-=at
        if monh <= 0:
            monh = 0
        print(f'Monster\'s HP left {monh}')
        if monh == 0:
            print('You win.(^_^)')
            break
    if myTurn == 'h':
        ch = 0
        meh+=20
        at = 10
        print(f'Your HP left {meh}')
    a = X.randint(1, 40)
    meh-=a
    if meh < 0:
        meh = 0
    print(f'Monster\'s turn : Your HP left {meh}')
    if meh <= 0:
        print('You lose and die.(T_T)')
        break