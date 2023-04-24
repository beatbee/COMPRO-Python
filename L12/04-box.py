n = int(input('N: '))
one,two,three = 0,0,0
for i in range(n):
    a = int(input(f'Order {i+1} A: '))
    b = int(input(f'Order {i+1} B: '))
    c = int(input(f'Order {i+1} C: '))
    lst = [a,b,c]
    lst.sort()
    A,B,C=lst[0],lst[1],lst[2]
    if A<=8 and B<=10 and C<=15:
        print('Box size 1')
        one+=1
    elif A<=12 and B<=15 and C<=25:
        print('Box size 2')
        two+=1
    elif A<=20 and B<=40 and C<=50:
        print('Box size 3')
        three+=1
    else:
        print('Oversize product')
if n >= 0:
    print(f'Use Box size 1: {one}')
    print(f'Use Box size 2: {two}')
    print(f'Use Box size 3: {three}')