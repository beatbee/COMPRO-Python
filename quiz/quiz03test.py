grid1 = [['.','.','.','.','.','.'],
         ['.','o','o','.','.','.'],
         ['o','o','o','o','.','.'],
         ['o','o','o','o','o','.'],
         ['.','o','o','o','o','o'],
         ['o','o','o','o','o','.'],
         ['o','o','o','o','.','.'],
         ['.','o','o','.','.','.'],
         ['.','.','.','.','.','.']]
grid2 = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','o','.','o'],
         ['o','o','.','o','.','o','.'],
         ['o','o','o','o','o','.','.'],
         ['o','o','.','o','.','o','.'],
         ['.','.','.','.','o','.','o'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.']]
grid3 = [[' ',' ',' ',' ','o','o',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         ['o',' ',' ',' ','o','o','o','o','o',' ',' '],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ']]
def rotate_left(grid):
    left = []
    new = []
    for i in range(len(grid[0])-1,-1,-1):
        left = []
        for j in range(len(grid)):
            left.append(grid[j][i])
        new.append(left)
    return new
def rotate_right(grid):
    right = []
    new = []
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            right.append(grid[len(grid)-j-1][i])
        new.append(right)
        right = []
    return new
def mirror(grid):
    turn = []
    new = []
    for i in range(len(grid)):
        for j in range(len(grid[0])-1,-1,-1):
            turn.append(grid[i][j])
        new.append(turn)
        turn = []
    return new
def rotate_180(grid):
    new=[]
    for i in range(len(grid)):
        row=[]
        for j in range(len(grid[0])):
            row.append(grid[i][len(grid[0])-j-1])
        new.append(row)
    return new
    

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end='')
        print()
print_grid(rotate_180(grid2))
"""
grid1 = [['.','.','.','.','.','.'],
         ['.','o','o','.','.','.'],
         ['o','o','o','o','.','.'],
         ['o','o','o','o','o','.'],
         ['.','o','o','o','o','o'],
         ['o','o','o','o','o','.'],
         ['o','o','o','o','.','.'],
         ['.','o','o','.','.','.'],
         ['.','.','.','.','.','.']]

grid2 = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','o','.','o'],
         ['o','o','.','o','.','o','.'],
         ['o','o','o','o','o','.','.'],
         ['o','o','.','o','.','o','.'],
         ['.','.','.','.','o','.','o'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.']]

grid3 = [[' ',' ',' ',' ','o','o',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         ['o',' ',' ',' ','o','o','o','o','o',' ',' '],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ']]

def rotate_left(grid) :
    newrow = len(grid[0])
    newcolumn = len(grid)
    newGrid = [['.']*newcolumn for i in range(newrow)]
    for i in range(newrow) :
        for j in range(newcolumn) :
            newGrid[i][j] = grid[j][newrow-i-1]
    return newGrid

def rotate_right(grid) :
    newrow = len(grid[0])
    newcolumn = len(grid)
    newGrid = [['.']*newcolumn for i in range(newrow)]
    for i in range(newrow) :
        for j in range(newcolumn) :
            newGrid[i][j] = grid[newcolumn-j-1][i]
    return newGrid

def rotate_180(grid) :
    row,column = len(grid),len(grid[0])
    newGrid = [[' ']*column for i in range(row)]
    for i in range(row) :
        for j in range(column) :
            newGrid[i][j] = grid[row-i-1][column-j-1]
    return newGrid

def mirror(grid) :
    row,column = len(grid),len(grid[0])
    newGrid = [[' ']*column for i in range(row)]
    for i in range(row) :
        for j in range(column) :
            newGrid[i][j] = grid[i][column-j-1]
    return newGrid

def print_grid(grid) :
    row = len(grid)
    column = len(grid[0])
    for i in range(row) : 
        for j in range(column) :
            print(grid[i][j],end='')
        print()
print_grid(mirror(grid2))
"""

