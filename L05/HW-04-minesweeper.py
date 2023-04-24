m,n = [int(x) for x in input("Grid Size: ").split()]
x = int(input("Number of mine(s): "))
mine = [[0]*m for i in range(n)]
for i in range(x):
    a,b = [int(x) for x in input(f"Mine#{i+1}: ").split()]
    mine[b][a] = 'X'
def checkbomb(x,y):
    ans = 0
    if x+1<n and mine[x+1][y] == 'X' : ans+=1
    if x-1>=0 and  mine[x-1][y] == 'X' : ans+=1
    if y+1<m and mine[x][y+1] == 'X': ans+=1
    if y-1>=0 and mine[x][y-1] == 'X' : ans+=1
    if x+1<n and y+1<m and mine[x+1][y+1] == 'X': ans+=1
    if x+1<n and y-1>=0 and mine[x+1][y-1] == 'X':ans+=1
    if x-1>=0 and y+1<m and mine[x-1][y+1] == 'X':ans+=1
    if x-1>=0 and y-1>=0 and mine[x-1][y-1] == 'X' : ans+=1
    return ans

for i in range(n):
    for j in range(m):
        if mine[i][j] == 0:
            num = checkbomb(i,j)
            mine[i][j] = num

for i in range(n):
    for j in range(m):
        print(mine[i][j],end=' ')
    print()

