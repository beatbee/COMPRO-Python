ans = 0
c = 100
h = 1
while(True):
    n = int(input('Input distance: '))
    ans+=n
    print(f'Police distance: {ans}')
    c += (2**h)
    print(f'Criminal distance: {c}')
    if(ans >= c):
        print('Caught him!')
        break
    h+=1
    