import json
file = input('Enter json filename : ')
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
#print(s['products'][0])
goods = {}
for i in s['products']:
    goods[i['product_name']] = int(i['price'])
cus = {}
for i in s['customers']:
    ans = 0
    for j in i['order']:
        ans += i['order'][j]*goods[j] 
    cus[i['customer_name']] = i['money']-ans
for i in sorted(cus):
    print(i)
    if cus[i] == 0:
        print('no change')
    if cus[i] >= 1000:
        n = cus[i]//1000
        print(f'1000 : {n}')
        cus[i]%=1000
    if cus[i] >= 500:
        n = cus[i]//500
        print(f'500 : {n}')
        cus[i]%=500
    if cus[i] >= 100:
        n = cus[i]//100
        print(f'100 : {n}')
        cus[i]%=100
    if cus[i] >= 50:
        n = cus[i]//50
        print(f'50 : {n}')
        cus[i]%=50
    if cus[i] >= 20:
        n = cus[i]//20
        print(f'20 : {n}')
        cus[i]%=20
    if cus[i] >= 10:
        n = cus[i]//10
        print(f'10 : {n}')
        cus[i]%=10
    if cus[i] >= 5:
        n = cus[i]//5
        print(f'5 : {n}')
        cus[i]%=5
    if cus[i] >= 2:
        n = cus[i]//2
        print(f'2 : {n}')
        cus[i]%=2
    if cus[i] >= 1:
        print(f'1 : {cus[i]}')
    print()