m,n = [int(x) for x in input('City Size: ').split()]
new = []
lst = []
for i in range(m):
    x = [int(e) for e in input().split()]
    lst.append(x)
west = lst
north = []
for i in range(n):
    for j in range(len(lst)):
        new.append(lst[j][i])
    north.append(new)
    new = []
south= []
for i in range(n):
    for j in range(len(lst)-1,-1,-1):
        new.append(lst[j][i])
    south.append(new)
    new = []
east = []
for i in range(m):
    for j in range(n-1,-1,-1):
        new.append(lst[i][j])
    east.append(new)
    new = []
n,s,w,e = 1*n,1*n,1*m,1*m
#north south
for i in range(n):
    for j in range(len(lst)):
        if north[i][j] > north[i][0] and north[i][j] > north[i][j-1]:
            n+=1
        #print(north[i][j],north[i][0],n)
        if south[i][j] > south[i][0] and south[i][j] > south[i][j-1]:
            s+=1
#east west
#print(west)
for i in range(m):
    for j in range(len(lst[0])):
        if west[i][j] > west[i][0] and west[i][j] > west[i][j-1]:
            w+=1
        #print(west[i][j],west[i][j-1],west[i][0],w)
        if east[i][j] > east[i][0] and east[i][j] > east[i][j-1]:
            e+=1
check = {'N' : n,'S': s,'E': e,'W':w}
mx= max(n,e,w,s)
for i,j in check.items():
    if check[i] == mx:
        print(i,end=' ')
"""
4 5å
2 3 5 6 2
1 3 4 7 1
6 5 4 1 3
2 3 7 9 6
W
5 5
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
N S E W
"""