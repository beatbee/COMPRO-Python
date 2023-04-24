"""
def add(x,y,new):
    if x+1<m : new[x+1][y]*=1.1
    if x-1>=0: new[x-1][y]*=1.1
    if y+1<n : new[x][y+1]*=1.1
    if y-1>=0 : new[x][y-1]*=1.1
    return new
def moontuan(x,y):
    ans = 0
    new = build()
    ans+=new[x][y]
    new = add(x,y,new)
    x+=1
    ans+=new[x][y]
    new = add(x,y,new)
    y-=1
    ans+=new[x][y]
    new = add(x,y,new)
    x-=1
    ans+=new[x][y]
    return ans
def moontam(x,y):
    ans = 0
    new = build()
    ans+=new[x][y]
    new = add(x,y,new)
    x+=1
    ans+=new[x][y]
    new = add(x,y,new)
    y+=1
    ans+=new[x][y]
    new = add(x,y,new)
    x-=1
    ans+=new[x][y]
    return ans
def check(x,y):
    if (x+1<m) and y-1>=0: return 'tuan'
    if (x+1<m) and y+1<n: return 'tam'

def build():
    lst = []
    new = []
    for i in range(len(lst1[0])):
        for j in range(len(lst1)):
            new.append(lst1[j][i])
        lst.append(new)
        new = []
    return lst
"""
#########main########
lst = []
while True:
    land = [int(x) for x in input().split()]
    if land == []:
        break
    lst.append(land)
#lst = build()
x  = len(lst[0])
for i in range(len(lst)):
    y = len(lst[i])
    if x!=y:
        print('Can\'t Buy')
        exit(0)
m,n = len(lst),len(lst[0])
mn = 2e9
for i in range(m-1) :
    for j in range(n-1) :
        total = lst[i][j] + lst[i][j+1]*1.1 + lst[i+1][j+1]*1.1 + lst[i+1][j]*1.21
        mn = min(mn,total)
        total = lst[i+1][j] + lst[i+1][j+1]*1.1 + lst[i][j+1]*1.1 + lst[i][j]*1.21
        mn = min(mn,total)
print(f'{mn:.2f}')
"""
mn = 100000
good = []
c = 0
for i in range(m):
    for j in range(n):
        if check(i,j) == 'tam':
            #print(i,j,check(i,j))
            a = moontam(i,j)
            #print(f'Tam : {a}')
        if check(i,j) == 'tuan':
            #print(check(i,j))
            c = moontuan(i,j)
            #print(f'Tuan : {c}')
            #print(f'Yayyyy :{a}')
        if a==0 :
            w = c
        elif c == 0:
            w = a
        else:
            w= min(a,c)
        #print(f'Min : {w}')
        good.append(w)
print(f'{min(good):.2f}')
"""
"""
10 12 50
50 40 20

"""