""""
class Car:
    def __init__(self, license, brand, color):
        self.license = license
        self.brand = brand
        self.color = color
        self.report = []
    def __str__(self):
        return self.license + ' - ' + self.color + ', ' + self.brand

    def __lt__(self, rhs):
        return self.license < rhs.license
    # เรียงลำดับรถยนต์โดยเปรียบเทียบป้ายทะเบียนรถแบบสตริง

    def add_report(self, new_report):
        self.report.append(new_report)

    # เพิ่มประวัติการซ่อมบำรุง โดยไม่ต้องคืนค่า
    # ตัวแปร new_report เก็บ tuple (วันที่, คำอธิบาย, ราคา)
    # เช่น c.add_report( ('25 May 2017', 'change tires', 1500) )
    def total_payment(self):
     return sum(r[2] for r in self.report)
    def max_payment(self):
        mx = -1
        for r in self.report:
            if int(r[2]) > mx:
                mx = int(r[2])
        print(f'Max maintainance: {self.__str__()}')
        if mx == -1:
            print('No maintainance')
        else:
            for i in self.report:
                print(f'Date: {i[0]}, Maintenace: {i[1]}, Cost: {i[2]}')
                

    def print_report(self):
        for i in range(len(self.report)):
            print(f'Date: {self.report[i][0]}, Maintenace: {self.report[i][1]}, Cost: {self.report[i][2]}')
        total = self.total_payment()
        print(f'Total maintenance: {total}')
    mport json
class Account:
  def __init__(self, name, accnb, money, history):
    self.name = name; self.accnb = accnb; self.money = money
    self.history = history
  def __str__(self):
    return f'Name : {self.name}\nAccount number : {self.accnb}\nMoney : {self.money}'
  def show_data(self):
    print(self.__str__())
    if self.history['deposit']==0 and self.history['withdraw']==0:
      print('History')
    else:
      print(f'History : Deposit : {self.history["deposit"]}\nWithdraw : {self.history["withdraw"]}')
  
def readJsonData():
  myAccount = []
  ss = json.loads(s)
  for i in range(len(ss)):
    #print(ss[i])
    name, accNb, money, history = ss[i]['name'], ss[i]['account number'], ss[i]['money'], ss[i]['history']
    a = Account(name, accNb, money, history)
    myAccount.append(a)
    #print(a)
  return myAccount
def menuOne(myAccount):
  accNb = input('Account number : ')
  for m in myAccount:
    if m.accnb == accNb:
      m.show_data()      

    
myCar = []
car1 = Car('AA1234', 'Honda', 'White')
car2 = Car('NN5678', 'Nissan', 'Blue Navi')
car3 = Car('BB9999', 'Lambogini', 'Yellow')
myCar.append(car1)
myCar.append(car2)
myCar.append(car3)
for c in myCar:
  print(c)
print()
for c in sorted(myCar, reverse=True):
  print(c)
print()
car2.add_report(('25 May 2017', 'change tires', 1500))
car2.add_report(('2 June 2017', 'change lamp head', 1000))
car2.print_report()
car2.total_payment()
print()
car2.add_report(('20 July 2017', 'change dish brake', 1500))
car2.max_payment()
print()
car1.max_payment()
"""
"""
class ShoppingCart:
  def __init__(self, id):
    self.id = id
    self.books = []
    self.books = id
    # books เก็บลิสต์ของหนังสือในตะกร้าพร้อมจำนวน เช่น [[b1,2],[b3,7]]
  def add_book(self, book, n):
    for i in self.books:
        if i[0] == book:
            i[1] += n
            break
        else:
            self.books.append([book,n])
    # เพิ่มข้อมูลการซื้อหนังสือ book เพิ่มอีก n เล่ม โดยไม่ต้องคืนค่า
    # หากไม่มีหนังสือเล่มนี้ในตะกร้า ให้เพิ่มลิสต์ [book, n] ต่อท้าย books
    # หากเคยมีข้อมูลหนังสือเล่มนี้ในตะกร้าแล้ว ให้เพิ่มจำนวนที่ซื้ออีก n เล่ม
    # เช่น ถ้า books = [[b1,2]] และเราสั่ง add_book(b1,3) จะได้ books = [[b1,5]]
  def get_total(self):
    return sum([b.price*n for [b,n] in self.books])
  def __lt__(self, rhs):
    return self.get_total() < rhs.get_total()
  def print_book(self):
        for i in range(len(self.books)):
            print(f'Date: {self.books[i][0]}')

b2 = ShoppingCart('b2')
b1 = ShoppingCart('b1')
b1.add_book(b1,2)
b1.add_book(b1,3)
b1.print_book()
"""
class Card:
    card = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    score = [3,4,5,6,7,8,9,10,10,10,10,1,2]
    suit = ['club','diamond','heart','spade']
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'({self.value},{self.suit})'
    def getScore(self):
        #return self.value
        return Card.score[Card.card.index(self.value)]
    def sum(self,other):
        return (self.getScore()+other.getScore())%10
    def __lt__(self, rhs):
        if self.getScore() != rhs.getScore(): #rhs righthandside
            return self.getScore() < rhs.getScore()
        else:
            return Card.suit.index(self.suit) < Card.suit.index(rhs.suit)


inputCard = ['A spade','K heart','K club','7 diamond','2 spade']
cards = []
for i in range(len(inputCard)):
    j = inputCard[i].split()
    value,suit = j[0],j[1]
    c = Card(value,suit)
    print(c,c.getScore())
    cards.append(c)
print()
for i in range(len(cards)-1):
    print(cards[i].sum(cards[i+1]))
    print(Card.sum(cards[i],cards[i+1]))
for i in sorted(cards,reverse=True):
  print(i,i.getScore())

"""
parentthesis
alist,blist,clist = [],[],[]
s = '(()a(){{}s[][d]f}g)'
for i in s:
  if i=='(':
    alist.append(i)
  elif i=='[':
    blist.append(i)
  elif i=='{':
    clist.append(i)
  elif i==')':
    if alist[len(alist)-1]=='(': # check balance 
      del alist[len(alist)-1]
  else:
    continue
if len(alist)==0:
  print(f'( balanced')
else:
  print(alist)
if len(blist)==0:
  print(f'[ balanced')
else:
  print(blist)
if len(clist)==0:
  print(f'{{ balanced')
else:
  print(clist)
"""




