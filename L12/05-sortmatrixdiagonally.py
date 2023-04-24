def printmat(mat):
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      print(mat[i][j], end = " ")
    print()
m = int(input('M: '))
n = int(input('N: '))
lst = [[0]*n for i in range(m)]
D = {}
for i in range(m):
    a =[int(x) for x in input().split()]
    for j in range(n):
        if i-j not in D:
            D[i-j] = []
        D[i-j].append(a[j])
    for k in D:
        D[k].sort()
ch = 0
for i in range(m):
    for j in range(n):
        x = D[i-j][ch]
        lst[i][j] = x
        D[i-j].remove(D[i-j][0])
print('sorted matrix is:')
printmat(lst)
