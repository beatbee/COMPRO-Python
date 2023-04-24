n = int(input())
m=int(input())
word = []
for i in range(n):
    x = [e for e in input().split()]
    word.append(x)
lst = [[' ' for i in range(n+m-1)] for j in range(n+m-1)]
sx = 0
if n==m:
    sy = (n+m-1)//2
else:
    sy = (n+m-1)//2 - 1
for i in word:
    x= sx
    y = sy
    for j in range(len(i)):
        if j == 0:
            sx = x
            sy = y
        lst[x][y] = i[j]
        x+=1
        y+=1
    sx+=1
    sy-=1
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j],end=' ')
    print()

