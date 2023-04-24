def sum_price():
    total = 0
    print("Menu")
    print("0. Finish")
    print("1. Latte = 40")
    print("2. Espresso = 45")
    print("3. Americano = 50")
    print("4. Mocca = 55")
    print("5. Cappuccino = 60")
    while(True):
        coffee = int(input("coffee : "))
        if coffee == 0:
            break
        if coffee == 1:
            num = 40
        elif coffee == 2:
            num = 45
        elif coffee == 3:
            num = 50
        elif coffee == 4:
            num = 55
        elif coffee == 5:
            num = 60
        amount = int(input("amount : "))
        total += (num*amount)
    print(f"total price : {total}")
    return total
def change(total_price,pay):
    ans = pay - total_price
    print(f"customer's change : {ans}")
    while ans >= 0:
        if ans >=1000:
            n = ans//1000
            ans%=1000
            print(f"change 1000 : {n}")
        elif ans >=500:
            n = ans//500
            print(f"change 500 : {n}")
            ans = ans%500
        elif ans >=100:
            n = ans//100
            print(f"change 100 : {n}")
            ans = ans%100
        elif ans >=50:
            n = ans//50
            print(f"change 50 : {n}")
            ans = ans%50
        elif ans >=20:
            n = ans//20
            print(f"change 20 : {n}")
            ans = ans%20
        elif ans >=10:
            n = ans//10
            print(f"change 10 : {n}")
            ans = ans%10
        elif ans >=5:
            n = ans//5
            print(f"change 5 : {n}")
            ans = ans%5
        else:
            break
    return ans

total = 0      
n = sum_price()
pay = int(input("customer pay : "))
change(n,pay)
