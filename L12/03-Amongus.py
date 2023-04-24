n = int(input('Input n: '))
m = int(input('Input m: '))
a = []
for i in range(n):
    lst = [int(x) for x in input().split()]
    a.append(lst)
for i in range(1,n*m+1):
    for j in range(n):
        for k in range(m):
            if a[j][k] == i:
                print(f'({j},{k})')