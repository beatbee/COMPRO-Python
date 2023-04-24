m = int(input('Input the maze\'s size (only 1 to 9): '))
op = int(input('Input the type of maze (only 1 to 2): '))
lst = [[0]*(2*m-1) for i in range(2*m-1)]
if op == 1:
    nub = 1
    a = 0
    for k in range(m):
        for i in range(a,2*m-1-a):
            for j in range(a,2*m-1-a):
                lst[i][j] = nub
        if m%2 == 0:
            if nub ==m-1:
                nub=0
        else:
            if nub == m:
                nub = 0
        nub+=2
        a+=1
if op == 2:
    if m == 1:
        nub = 1
    else:
        nub = 2
    a = 0
    for k in range(m):
        for i in range(a,2*m-1-a):
            for j in range(a,2*m-1-a):
                lst[i][j] = nub
        if m%2 == 1:
            if nub ==m-1:
                nub=-1
        else:
            if nub == m:
                nub=-1
        nub+=2
        a+=1
for i in range(2*m-1):
    for j in range(2*m-1):
        print(lst[i][j],end=' ')
    print()


