n = int(input())
lst = [[0]*(2*n-1) for i in range(2*n-1)]
a = 0
for k in range(n,0,-1):
    for i in range(a,2*n-1-a):
        for j in range(a,2*n-1-a):
            lst[i][j] = k
    a+=1
for i in range(2*n-1):
    for j in range(2*n-1):
        print(lst[i][j],end=' ')
    print()
