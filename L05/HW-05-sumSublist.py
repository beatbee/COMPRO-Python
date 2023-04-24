num = [int(x) for x in input().split()]
while(True):
    x,y = [int(x) for x in input().split()]
    ch = 0
    if x< -len(num) and y > len(num)-1 or y< -len(num) and x > len(num)-1:
        print('x and y Bad Input')
        ch = 1
    elif x< -len(num):
        print('x Bad Input')
        ch =1
    elif y > len(num)-1:
        print('y Bad Input')
        ch = 1
    if x<0: x+=len(num)
    if y<0: y+=len(num)
    if x>y: break
    if(ch == 0):
        ans = 0
        for i in range(x,y+1):
            ans+=num[i]
        print(ans)