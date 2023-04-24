def testlist():
    print('Customer name : Belle')
    order = {'hamburger' : '900 baht' , 'chicken' : '700 baht', 'spagetti' : '500 baht' , 'kfc' : '20 baht'}
    print(order)
    print("Total = 100000 ")
    print('discount : 20%')
    print("last total: 10000 ")
    print("Pay : 10000")
    print("change : 0")
def printmenu():
    s,cnt = '',1
    for i,j in orderlst.items():
        s+=f'[{cnt}] | {i:<13} | {j} baht'
        print(s)
        cnt+=1
        s=''
def cuschange(pay,sum):
    change = pay-sum
    if change>=1000:
        n = change//1000
        change%=1000
        print(f'1000 : {n}')
    if change>=500:
        n = change//500
        change%=500
        print(f'500 : {n}')
    if change>=100:
        n = change//100
        change%=100
        print(f'100 : {n}')
    if change>=50:
        n = change//50
        change%=50
        print(f'50 : {n}')
    if change>=20:
        n = change//20
        change%=20
        print(f'20 : {n}')
    if change>=10:
        n = change//10
        change%=10
        print(f'10 : {n}')
    if change>=5:
        n = change//5
        change%=5
        print(f'5 : {n}')
    if change>=1:
        print(f'1 : {change}')
    chanage1 = pay -sum
    return chanage1
def checkdis(sum):
    if sum >= 1000:
        dis = 10
    elif sum >= 500:
        dis = 20
    else:
        dis = 0
    total = sum*(100-dis)/100
    return dis,total
def printorder(customer):
    print('------------------------------')
    for i,j in customer.items():
        print(f'Customer : {i}')
        print(j)
        print(f'Total : {calprice(j)} baht')
        x,y = checkdis(calprice(j))
        print(f'Discount: {x}%')
        print(f'Lasttotal : {y} baht')
        pay = int(input("Pay : "))
        a = cuschange(pay,calprice(j))
        print(f'change : {a}')
        print('------------------------------')
def calprice(order):
    sum = 0
    for i,j in order.items():
        sum+=j[1]
    return sum

def getorder():
    order = {}
    num = {'Hamburger' : 0,'fried chicken' : 0,'frenchfries' : 0,'Potato kick' : 0,'egg tart' : 0,'happy meal' : 0,'full meal' : 0,'family meal' : 0}
    while True:
        printmenu()
        n = int(input("Choose your order or 0 to exit: "))
        if n == 0:
            break
        elif n not in range(1,9):
            print("Choose only 1-8 to order or 0 to exit")
        elif lst[n-1] in order:
            cnt = num[lst[n-1]]+1
            print(cnt)
            order[lst[n-1]][0] = num[lst[n-1]]+1
            order[lst[n-1]][1] = orderlst[lst[n-1]]*cnt
            num[lst[n-1]]+=1
            #order[lst[n-1]].append(num[lst[n-1]]+1)
            #order[lst[n-1]].append(orderlst[lst[n-1]]*cnt)
            print(order)
        else:
            order[lst[n-1]] = [num[lst[n-1]]+1,orderlst[lst[n-1]]]
            num[lst[n-1]]+=1
            print(order)
        cnt = 0
    return order

def cusorder():
    customer = {}
    while True:
        name = input("Enter your name or press Enter to exit : ")
        if name == '':
            break
        elif name in customer:
            print("This name is already order")
        else:
            x = getorder()
            customer[name] = x
            y = calprice(x)
            print(name , customer[name])
            print(f'Total : {y}')
    return customer
lst = ['Hamburger','fried chicken','frenchfries','Potato kick','egg tart','happy meal','full meal','family meal']
orderlst = {'Hamburger' : 50,'fried chicken' : 45,'frenchfries' : 32,'Potato kick' : 47,'egg tart' : 24,'happy meal' : 119,'full meal' : 239,'family meal' : 339}
a = cusorder()
printorder(a)