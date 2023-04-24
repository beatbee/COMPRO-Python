word = input('Enter a string, such as "ILoveYou" : ')
n = len(word)
a= 0
b = 0
sx = (2*n)-2
sy = (2*n)//2-1
sx1 = 0
sy1 = (2*n)//2-1
lst = [[' ']*(2*len(word)-1) for i in range(2*len(word)-1)]
for k in word:
    x = sx1
    y = sy1
    x1 = sx
    y1 = sy
    for i in range(1,n+1-a):
        lst[x][y] = k
        x+=1
        y-=1
    x = sx1
    y = sy1
    for i in range(1,n+1-a):
        lst[x][y] = k
        x+=1
        y+=1
    for i in range(1,n-a):
        lst[x1][y1] = k
        x1-=1
        y1-=1
    x1 = sx-1
    y1 = sy+1
    for i in range(1,n-a):
        lst[x1][y1] = k
        x1-=1
        y1+=1
    sx1+=1
    sx-=1
    a+=1
for i in range(2*len(word)-1):
    for j in range(len(lst[i])):
        print(lst[i][j],end=' ')
    print()