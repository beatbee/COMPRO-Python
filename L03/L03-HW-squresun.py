def draw(n):
    #top
    j = 0
    for i in range(n-2,-1,-1):
        print(' '*(j)+'*' + ' '*(n+2*(i)) +'*')
        j+=1
    #mid
    print(' '*(n-1)+'*'*n)    
    for i in range(n-2):
        print(' '*(n-1)+'*' + ' '*(n-2) + '*')
    print(' '*(n-1)+'*'*n)
    #bottom
    j = n-2
    for i in range(n-1):
        print(' '*(j)+'*' + ' '*(n+2*(i)) +'*')
        j-=1

n = int(input())
draw(n)