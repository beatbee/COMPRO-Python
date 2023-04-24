def printmenu():
    print('Coffee Menu')
    print('0. Finish')
    print('1. Latte = 40')
    print('2. Espresso = 45')
    print('3. Americano = 50')
    print('4. Mocca = 55')
    print('5. Cappuccino = 60')
def order_coffee():
    orders_dict = {}
    total_price = 0
    while True:
        n = int(input("Coffee type: "))
        if n == 0:
            break
        if n == 1:
            c = 'Latte'
            t = 40
        if n == 2:
            c = 'Espresso'
            t = 45
        if n == 3:
            c = 'Americano'
            t = 50
        if n == 4:
            c = 'Mocca'
            t = 55
        if n == 5:
            c = 'Cappuccino'
            t = 60
        amount = int(input(f"Amount of {c} : "))
        if c in orders_dict:
            orders_dict[c] += amount
        else:
            orders_dict[c]= amount
        total_price+=t*amount
    print(f'Total price: {total_price}')
    return orders_dict,total_price
def change(total_price, pay):
    change = pay - total_price
    print(f'Customer\'s change: {change} ')
    if change >= 1000:
        n = change//1000
        print(f'Change 1000 : {n}')
        change%=1000
    if change >= 500:
        n = change//500
        print(f'Change 500 : {n}')
        change%=500
    if change >= 100:
        n = change//100
        print(f'Change 100 : {n}')
        change%=100
    if change >= 50:
        n = change//50
        print(f'Change 50 : {n}')
        change%=50
    if change >= 20:
        n = change//20
        print(f'Change 20 : {n}')
        change%=20
    if change >= 10:
        n = change//10
        print(f'Change 10 : {n}')
        change%=10
    if change >= 5:
        n = change//5
        print(f'Change 5 : {n}')
        change%=5
    if change >= 1:
        #n = change//1000
        print(f'Change 1 : {change}')
def print_receipt(orders_dict, customer_name, total_price):
    print('--------- receipt ---------')
    print('CPE35 COFFEE SHOP')
    print(f'Customer name: {customer_name}')
    for i,j in orders_dict.items():
        print(f'{i} {j}',end=', ')
    print(f'{total_price} baht')
    print('Thank you')
    print('---------------------------')
def print_report(sales_dict):
    total = 0
    print('---- Daily Sale Report ----')
    for i,j in sales_dict.items():
        print(f'{i} {j} baht')
        total+=j
    print(f'Total sale: {total} baht')
    print('---------------------------')
customer = {}
while True:
    printmenu()
    name = input('Customer name: ')
    if name == 'end day':
        print_report(customer)
        break
    order,total = order_coffee()
    if name in customer:
        customer[name] +=total
    else:
        customer[name] = total
    pay = int(input("Customer pay: "))
    change(total,pay)
    print_receipt(order,name,total)




