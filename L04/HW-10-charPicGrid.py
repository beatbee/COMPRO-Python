def print_grid(grid):
     for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j],end='')
        print()
def rotate_left(grid):
    newleft = []
    new = []
    for i in range(len(grid[0])-1,-1,-1):
        for j in range(len(grid)):
            newleft.append(grid[j][i])
        new.append(newleft)
        newleft = []
    return new


def rotate_right(grid):
    newright = []
    new = []
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            newright.append(grid[len(grid)-j-1][i])
        new.append(newright)
        newright = []
    return new

        

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


