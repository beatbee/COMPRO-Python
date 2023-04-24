def printmenu():
    print("Select menu :")
    print("1. add flight data")
    print("2. flight data by code")
    print("3. show all flight data")
    print("4. flight booking")
    print("5. show people flight data")
    print("6. exit")
def menu1(allflight,n):
    data = [x for x in input("Add data : ").split()]
    data.remove('->')
    j = 0
    for i in data:
        if i == '/':
            l = j
        j+=1
    lst = []
    x = int(''.join(data[3:l]))
    y = int(''.join(data[l+1:]))
    lst.append(x)
    lst.append(y)
    allflight[data[0]] = data[1:]
    n[data[0]] = lst
    #print(n)
def menu2(a,n):
    code = input("Enter code : ")
    print(f'{code} is from {a[code][0]} to {a[code][1]}, number of people booking is {n[code][0]}/{n[code][1]}')
def menu3(a,n):
    print("All flight data")
    for code in a:
        print(f'{code} is from {a[code][0]} to {a[code][1]}, number of people booking is {n[code][0]}/{n[code][1]}')
def menu4(flight,costumer):
    name = input("Enter your name : ")
    code = input("Enter flight code : ")
    if(flight[code][0] == flight[code][1]):
        print("The flight is full, Sorry")
    else:
        if name in costumer:
            #costumer[name].append(code)
            costumer[name] += f' {code}'
        else:
            #costumer[name] = [code]
            costumer[name] = f'{code}'
        print("Success")
        flight[code][0]+=1
def menu5(name):
    n = input("Enter your name : ")
    if n in name:
        #print(f"{n} is booking flight code = {' '.join(name[n])}")
        print(f"{n} is booking flight code = {name[n]}") #เหลือตรงที่book ซ้ำ แต่ไม่แสดง
printmenu()
allflight = {}
costumer = {}
number = {}
while(True):
    m = int(input("menu : "))
    if m == 1: x= menu1(allflight,number)
    if m == 2: x = menu2(allflight,number)
    if m == 3: x = menu3(allflight,number)
    if m == 4: x = menu4(number,costumer)
    if m == 5: x = menu5(costumer)
    if m == 6:
        print("EXIT!!!!!!!!!!!!!!!")
        break
"""
test case:
menu : 1
Add data : 00x541d aaaa -> bbbb 0 / 50
menu : 1
Add data : 00x578x cccc -> dddd 100 / 100
menu : 1
Add data : 00x579q eeee -> uuuu 49 / 50
menu : 2
Enter code : 00x579q
00x579q is from eeee to uuuu, number of people booking is 49/50
menu : 2
Enter code : 00x578x
00x578x is from cccc to dddd, number of people booking is 100/100
menu : 3
All flight data
00x541d is from aaaa to bbbb, number of people booking is 0/50
00x578x is from cccc to dddd, number of people booking is 100/100
00x579q is from eeee to uuuu, number of people booking is 49/50
menu : 1
Add data : 00x579w eeee -> uuuu 20 / 50
menu : 3
All flight data
00x541d is from aaaa to bbbb, number of people booking is 0/50
00x578x is from cccc to dddd, number of people booking is 100/100
00x579q is from eeee to uuuu, number of people booking is 49/50
00x579w is from eeee to uuuu, number of people booking is 20/50
menu : 4
Enter your name : SomSak
Enter flight code : 00x578x
The flight is full, Sorry
menu : 4
Enter your name : Argin
Enter flight code : 00x579q
Success
menu : 4
Enter your name : Argin
Enter flight code : 00x541d
Success
menu : 4
Enter your name : SomSak
Enter flight code : 00x579q
The flight is full, Sorry
menu : 4
Enter your name : SomSak
Enter flight code : 00x541d
Success
menu : 5
Enter your name : SomSak
SomSak is booking flight code = 00x541d
menu : 5
Enter your name : Argin
Argin is booking flight code = 00x579q 00x541d
menu : 6
EXIT!!!!!!!!!!!!!!!
"""