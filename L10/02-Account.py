import json
class Account:
    def __init__(self,name,accnum,money,history):
        self.name = name ; self.accnum = accnum ; self.money = money 
        self.history = history
    def show_data(self):
        print(f'Name : {self.name}')
        print(f'Account number : {self.accnum}')
        print(f'Money : {self.money}')
        print(f'History : {self.history}')
    def deposit(self):
        a = int(input('Amount : '))
        self.money += a
        print(f'Current money : {self.money}')
        if self.history == '': self.history = f"Deposit : {a}"
        else : self.history+=f"\nDeposit : {a}"
    def withdraw(self):
        a = int(input('amount : '))
        self.money -= a
        print(f'Current money : {self.money}')
        if self.history == '' : self.history = f"Withdraw : {a}"
        else : self.history += f"\nWithdraw : {a}"
    def show_history(self):
        print(self.history)

file = input('Filename : ')
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
classes = []
for i in s:
    name,accnum,money,history = i['name'],i['account number'],i['money'],i['history']
    data = Account(name,accnum,money,history)
    classes.append(data)
def accc():
    acc = input('Account number : ')
    for i in classes:
        if i.accnum == acc:
            return i
i = accc()
while True:
    n = int(input('Menu : '))
    if n == 0:
        break
    elif n == 1:
        i.show_data()
    elif n == 2:
        i.deposit()
    elif n == 3:
        i.withdraw()
    elif n == 4:
        i.show_history()
    elif n == 5:
        i = accc()
        



