h = int(input('hight of electric poles : '))
n = int(input('number of electric poles : '))
max1 = 0
ans = 0
for i in range(n):
    l = int(input())
    if l > max1:
        max2 = max1
        max1 = l
    elif l > max2:
        max2 = l
    ans+=l
b = max1//max2
if max1 < max2*3 :
    ans = ans//n
    print('Avg :',ans)
    if(h<=1):
        if(ans >= 1000):
            print('YES',ans-1000)
        else:
            print('NO')
    elif(h<=4):
        if(ans >= 5000):
            print('YES',ans-5000)
        else:
            print('NO')
    elif(h<=8):
        if(ans >= 30000):
            print('YES',ans-30000)
        else:
            print('NO')
    elif(h>8):
        if(ans >= 75000):
            print('YES',ans-75000)
        else:
            print('NO')
else:
    ans = (ans-(max1))//(n-1) + (max1//b)
    print('Avg :',ans)
    if(h<=1):
        if(ans >= 3000):
            print('YES',ans-3000)
        else:
            print('NO')
    elif(h<=4):
        if(ans >= 10000):
            print('YES',ans-10000)
        else:
            print('NO')
    elif(h<=8):
        if(ans >= 50000):
            print('YES',ans-50000)
        else:
            print('NO')
    elif(h>8):
        if(ans >= 100000):
            print('YES',ans-100000)
        else:
            print('NO')



    