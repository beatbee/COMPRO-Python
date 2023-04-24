def check(x,y):
    for i in range(x,x+4):
        for j in range(y,y+2):
            if j == w-1 or i == l-1:
                return 'no'
            if lst[i][j] == 0:
                return 'no'
    for i in range(x,x+4):
        for j in range(y,y+2):
            if j == w-1 or i == l-1:
                return 'no'
            if lst[i][j] == 1:
                lst[i][j] = 'x'
    return lst
def clear(x):
    for a in range(l):
        for b in range(w):
            if x[a][b] == 'x':
                x[a][b] = 1
    return x
l = int(input('Length: '))
w = int(input('Width: '))
lst = []
for i in range(l):
    court = [int(x) for x in input().split()]
    lst.append(court)
cnt = 0
for i in range(1,l-1):
    for j in range(1,w-1):
        if lst[i][j] == 1:
            x = check(i,j)
            if x != 'no':
                cnt+=1
                lst = clear(x)
print(f'{cnt} possible court(s)')
for i in range(1,l-1):
    for j in range(1,w-1):
        if lst[i][j] == 1:
            x = check(i,j)
            if x != 'no':
                for a in range(l):
                    for b in range(w):
                        print(x[a][b],end=' ')
                    print()
                lst = clear(x)
                print()

"""
0 0 0 0 
0 1 0 1 
0 1 1 1 
1 1 1 1 
0 1 1 1 
0 1 1 1 
0 1 1 0 
0 0 0 0
0 1 0 0 0 
0 1 0 1 1 
0 0 1 1 1 
1 1 0 1 1 
0 1 0 1 1 
0 0 1 1 1 
0 1 0 0 0
"""