n = int(input('number of electric poles : '))
max1 = 0
for i in range(n):
    l = int(input())
    if l > max1:
        max2 = max1
        max1 = l
    elif l > max2:
        max2 = l
if(max1 > max2*3):
    print('YES')
    print(max1)
else:
    print('NO')