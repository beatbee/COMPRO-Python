ask1 = input('Is Bulotelli injured?(y/n) ' )
if ask1 == 'y':
    print('Not available')
else:
    ask2 = input('Is Bulotelli late for the training?(y/n) ' )
    if ask2 == 'n':
        print('Starter')
    else:
        ask3 = input('Did Bulotelli perform well in training?(y/n) ')
        if ask3 == 'y':
            print('Substitute')
        else:
            print('Not selected')