file = input('File name: ')
price,order = {},{}
with open(file,'r') as fp:
    s = fp.read()
    print(s)
    for i in s.split('\n'):
        if i != '':
            w = i.split(' ')
            if i == 'Price':
                ch = 0
            if i == 'List':
                ch = 1
            if ch == 0 and w[0] !='Price' and w[0] != 'List':
                price[w[0]] = int(w[1])
            if ch == 1 and w[0] !='List' and w[0] !='Price':
                order[w[0]] = int(w[1])
            print(ch)
total = 0
for i in order:
    if i not in price:
        total+=0
    else:
        total += order[i]*price[i]
#print(price,order)
print(f'Total price: {total}')
#testcase03buylist.txt

