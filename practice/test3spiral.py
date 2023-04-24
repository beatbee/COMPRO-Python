word = input()
n = 1
while True:
    if n**2 >= len(word):
        break
    else:
        n += 2
lst = [['*' for x in range(n)] for y in range(n)]
print(lst)
x = y = n//2
ch = 1
check = 'm'
lst[x][y] = word[0]
for i in range(2,n,2):
    y+=1
    x+=1
    for j in range(i):
        if ch < len(word):
            x-=1
            lst[x][y] = word[ch]
            ch+=1
        else:
            break
    for j in range(i):
        if ch < len(word):
            y-=1
            lst[x][y] = word[ch]
            ch+=1
        else:
            break
    for j in range(i):
        if ch < len(word):
            x+=1
            lst[x][y] = word[ch]
            ch+=1
        else:
            break
    for j in range(i):
        if ch < len(word):
            y+=1
            lst[x][y] = word[ch]
            ch+=1
        else:
            break
for i in range(n):
  for j in range(n):
    print (lst[i][j] , end=" ")
  print()
