class Items:
    def __init__(self,id,type,price):
        self.id = id ; self.type = type ; self.price = price

m = int(input('How many products are there? : '))
lst = []
for i in range(m):
    x = [x for x in input().split()]
    id,type,price = x[0],x[1],x[2]
    data = Items(id,type,price)
    lst.append(data)
def checkid():
    while True:
        id = input('Id : ')
        ch = 0
        for i in lst:
            if i.id == id:
                ch = 1
                return i
        if ch == 0:
            print('This id doesn\'t exist.')
x = checkid()
while True:
    q = int(input('Q : '))
    if q == 1:
        print(x.type)
    elif q == 2:
        print(x.price)
    elif q == 3:
        x = checkid()
    elif q == 0:
        break

